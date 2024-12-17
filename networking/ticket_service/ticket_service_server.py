import asyncio
import json
import logging
import grpc

from classes.ticket_service import TicketService
from networking.airline import airline_service_pb2
from networking.airline.airline_service_pb2_grpc import AirlineServiceStub
from networking.ticket_service.ticket_service_pb2 import AbortReply, AbortRequest, BuyFlightPackageReply, CommitReply, CommitRequest, FlightsByRouteReply, VoteReply, VoteRequest
from networking.ticket_service.ticket_service_pb2_grpc import TicketServiceServicer, TicketServiceStub, add_TicketServiceServicer_to_server
from networking.utils.lamport_clock import LamportClock
from networking.utils.node_log import NodeLog

class TicketServiceServicer(TicketServiceServicer):

    def __init__(self, id):
        self.id = id
        self.ticket_service = TicketService()
        self.neighbor_clients = []
        self.airline_clients = []
        self.airline_flights = {}
        self.logs = []
        self.clock = LamportClock()
        self.vote_data = []

    def add_airline_clients(self, airline_clients):
        self.airline_clients = airline_clients
    
    def add_neighbor_clients(self, neighbor_clients):
        self.neighbor_clients = neighbor_clients

    async def GetFlightsByRoute(self, request, context):
        flights = await self._fetch_all_flights()
        flight_package = self.ticket_service.get_flights(flights, request.src, request.dest)
        return FlightsByRouteReply(flights=json.dumps(flight_package))

    async def BuyFlightPackage(self, request, context):
        flights_id = request.flights_id
        seats_amount = request.seats_amount

        await self._fetch_all_flights()
        
        log = NodeLog(flights_id, seats_amount, self.clock.get_time())
        self.logs.append(log)
        
        neighbor_votes = await self._collect_votes(flights_id, seats_amount)
        if not all(neighbor_votes):
            return await self._abort_transaction(log, "ERROR: Failed to get aprove from neighbors")

        reserve_results = await self._process_reservations(flights_id, seats_amount, self._reserve)

        if not all(request.is_temp_reserved for request in reserve_results):
            flights_to_cancel = [
                request.flight_id for request in reserve_results if request.is_temp_reserved
            ]
            await self._cancel_reserve(flights_to_cancel, seats_amount)
            await self._abort_transaction(log, "ERROR: can't reserve all the flights")
        
        await self._commit_transaction(log, flights_id, seats_amount)
        return BuyFlightPackageReply()

    async def Vote(self, request, context):
        await self._fetch_all_flights()
        seats_available = await self._get_seats_available(request.flights_id)
        if self._can_reserve(request.neighbor_id, request.flights_id, request.seats_amount, seats_available, request.timestamp):
            self.clock.update(request.timestamp)
            for flight_id in request.flights_id:
                self.vote_data.append((flight_id, request.seats_amount))
            return VoteReply(vote=True) #true is vote-commit
        else:
            return VoteReply(vote=False)

    async def Commit(self, request, context):
        self.clock.update(request.timestamp)
        for id in request.flights_id:
            if (id, request.seats_amount) in self.vote_data:
                self.vote_data.remove((id, request.seats_amount))
        return CommitReply()

    async def Abort(self, request, context):
        self.clock.update(request.timestamp)
        for id in request.flights_id:
            if (id, request.seats_amount) in self.vote_data:
                self.vote_data.remove((id, request.seats_amount))
        return AbortReply()


    async def _commit_transaction(self, log, flights_id, seats_amount):
        await self._process_reservations(flights_id, seats_amount, self._confirm_reserve) 
        self.clock.increment()        
        tasks = []        
        for neighbor in self.neighbor_clients:
            tasks.append(neighbor.Commit(CommitRequest(flights_id=flights_id, seats_amount=seats_amount, timestamp=self.clock.get_time())))
        await asyncio.gather(*tasks)
        log.set_status_committed()

    async def _abort_transaction(self, log, message):
        self.logs.remove(log)
        self.clock.increment()
        tasks = []        
        for neighbor in self.neighbor_clients:
            tasks.append(neighbor.Abort(AbortRequest(flights_id=log.flights_id, seats_amount=log.seats_amount, timestamp=self.clock.get_time())))
        await asyncio.gather(*tasks)
        return BuyFlightPackageReply(buy_success=False, message=message)

    async def _cancel_reserve(self, flights_id, seats_amount):
        tasks = []
        for flight_id in flights_id:
            airline_stub = self.airline_flights[flight_id]
            tasks.append(airline_stub.CancelReserve(
                airline_service_pb2.CancelReserveRequest(flight_id=flight_id, seats_amount=seats_amount)
                ))
        await asyncio.gather(*tasks)

    async def _collect_votes(self, flights_id, seats_amount):
        self.clock.increment()
        tasks = [
            asyncio.wait_for(
                neighbor.Vote(VoteRequest(flights_id=flights_id, seats_amount=seats_amount, timestamp=self.clock.get_time())),
                timeout=5
            )
            for neighbor in self.neighbor_clients
        ]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return [response.vote if isinstance(response, VoteReply) else False for response in responses]
    
    async def _fetch_all_flights(self):
        flights = []
        tasks = [self._get_airline_flights(airline, flights) for airline in self.airline_clients]
        await asyncio.gather(*tasks)
        return flights

    async def _get_airline_flights(self, airline, flights):
        response = await airline.GetAllFlights(airline_service_pb2.AllFlightsRequest())
        airline_flights = json.loads(response.all_flights)

        for flight in airline_flights:
            self.airline_flights[flight["id"]] = airline
            flights.append(flight)

    async def _process_reservations(self, flight_ids, seats_amount, reservation_func):
        tasks = [reservation_func(flight_id, seats_amount) for flight_id in flight_ids]
        return await asyncio.gather(*tasks)

    async def _reserve(self, flight_id, seats_amount):
        airline_stub = self.airline_flights[flight_id]
        response = await airline_stub.Reserve(
            airline_service_pb2.ReserveRequest(flight_id=flight_id, seats_amount=seats_amount)
        )
        return response

    async def _confirm_reserve(self, flight_id, seats_amount):
        airline_stub = self.airline_flights[flight_id]
        response = await airline_stub.ConfirmReserve(
            airline_service_pb2.ReserveRequest(flight_id=flight_id, seats_amount=seats_amount)
        )
        return response
            
    def _can_reserve(self, neighbor_id, flights_id, seats_amount, seats_available, timestamp):
        pending_logs = [
            log for log in self.logs if log.is_pending() and log.flight_id in flights_id 
        ]
        for log in pending_logs:
            if log.timestamp < timestamp:
                return False
            if log.timestamp == timestamp and self.id < neighbor_id:
                return False
        for flight in flights_id:
            if not self._check_seats(flight, seats_amount, seats_available):
                return False
        return True

    def _check_seats(self, flight_id, seats_amount, seats_available):
        seats = 0
        for flight_data in self.vote_data:
            if(flight_data[0] == flight_id):#log[0]->flight_id
                seats += flight_data[1]#log[1]->seats_reserved
        if(seats + seats_amount > seats_available[flight_id]):
            return False
        return True
    
    async def _get_seats_available(self, flights_id):
        seats_available = {}
        for f in flights_id:
            stub = self.airline_flights[f]
            response = await stub.GetSeatsAvailable(airline_service_pb2.SeatsAvailableRequest(flight_id=f))
            seats_available.update({f:response.seats_available})
        return seats_available

class TicketServiceServer:

    def __init__(self, port, airline_addresses, neighbor_addresses, id):
        self.port = port
        self.airline_addresses = airline_addresses
        self.neighbor_addresses = neighbor_addresses
        self.server = grpc.aio.server()
        self.ticket_service = TicketServiceServicer(id)

    async def start(self):
        logging.basicConfig()

        add_TicketServiceServicer_to_server(self.ticket_service, self.server)
        self.server.add_insecure_port(f"[::]:{self.port}")
        await self.server.start()
        self.ticket_service.add_airline_clients(await self._create_airline_clients(self.airline_addresses))
        self.ticket_service.add_neighbor_clients(await self._create_neighbor_clients())
        print(f"Server started, listening on {self.port}")
        await self.server.wait_for_termination()

    async def _create_neighbor_stub_with_retries(self, address, max_retries=5, retry_delay=1):
        for attempt in range(1, max_retries + 1):
            try:
                channel = grpc.aio.insecure_channel(address)
                await channel.channel_ready()
                return TicketServiceStub(channel)
            except Exception as e:
                if attempt == max_retries:
                    raise Exception(f"Failed to connect to {address} after {max_retries} attempts") from e
                print(f"Retrying connection to {address} (attempt {attempt}/{max_retries})...")
                await asyncio.sleep(retry_delay)

    async def _create_neighbor_clients(self):
        tasks = [self._create_neighbor_stub_with_retries(address) for address in self.neighbor_addresses]
        return await asyncio.gather(*tasks, return_exceptions=True)

    async def _create_airline_clients(self, airline_addresses):
        return [AirlineServiceStub(grpc.aio.insecure_channel(address)) for address in airline_addresses.values()]