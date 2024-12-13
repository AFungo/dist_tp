import asyncio
import json
import logging
import grpc

from classes.ticket_service import TicketService
from networking.airline import airline_service_pb2
from networking.airline.airline_service_pb2_grpc import AirlineServiceStub
from networking.ticket_service.ticket_service_pb2 import BuyFlightPackageReply, FlightsByRouteReply
from networking.ticket_service.ticket_service_pb2_grpc import TicketServiceServicer, add_TicketServiceServicer_to_server

class TicketServiceServicer(TicketServiceServicer):
    """
    Implements the TicketService gRPC service to manage ticket-related operations.
    """

    def __init__(self, airline_addresses):
        """
        Initializes the TicketServiceServicer with the given airline addresses.

        :param airline_addresses: A dictionary mapping airline names to their gRPC server addresses.
        """
        self.ticket_service = TicketService()
        self.airline_clients = self._create_airline_clients(airline_addresses)
        self.airline_flights = {}

    def _create_airline_clients(self, airline_addresses):
        """
        Creates gRPC clients for each airline address.
        :param airline_addresses: A dictionary of airline names and their gRPC addresses.
        :return: A list of AirlineServiceStub clients.
        """
        return [AirlineServiceStub(grpc.aio.insecure_channel(address)) for address in airline_addresses.values()]

    async def GetFlightsByRoute(self, request, context):
        """
        Handles the gRPC request to get all flight packages available for a given route.
        """
        flights = await self._fetch_all_flights()
        flight_package = self.ticket_service.get_flights(flights, request.src, request.dest)
        return FlightsByRouteReply(flights=json.dumps(flight_package))

    async def BuyFlightPackage(self, request, context):
        """
        Handles the gRPC request to buy a flight package (multiple flights).
        """
        flights = await self._fetch_all_flights()
        reserve_results = await self._process_reservations(request.flights_id, request.seats_amount, self._reserve)

        if not all(reserve_results):
            return BuyFlightPackageReply(buy_success=False, message="ERROR")

        confirm_results = await self._process_reservations(request.flights_id, request.seats_amount, self._confirm_reserve)

        if not all(confirm_results):
            return BuyFlightPackageReply(buy_success=False, message="ERROR")

        return BuyFlightPackageReply()

    async def _fetch_all_flights(self):
        """
        Fetch flights from all airline clients asynchronously.
        :return: A list of all flights.
        """
        flights = []
        tasks = [self._get_airline_flights(airline, flights) for airline in self.airline_clients]
        await asyncio.gather(*tasks)
        return flights

    async def _get_airline_flights(self, airline, flights):
        """
        Helper function to fetch flights from a specific airline asynchronously.
        """
        response = await airline.GetAllFlights(airline_service_pb2.AllFlightsRequest())
        airline_flights = json.loads(response.all_flights)

        for flight in airline_flights:
            self.airline_flights[flight["id"]] = airline
            flights.append(flight)

    async def _process_reservations(self, flight_ids, seats_amount, reservation_func):
        """
        Process reservations for the given flight IDs asynchronously.
        :param flight_ids: List of flight IDs to reserve.
        :param seats_amount: Number of seats to reserve.
        :param reservation_func: Function to handle reservation or confirmation.
        :return: List of results from the reservation function.
        """
        tasks = [reservation_func(flight_id, seats_amount) for flight_id in flight_ids]
        return await asyncio.gather(*tasks)

    async def _reserve(self, flight_id, seats_amount):
        airline_stub = self.airline_flights[flight_id]
        response = await airline_stub.Reserve(
            airline_service_pb2.ReserveRequest(flight_id=flight_id, seats_amount=seats_amount)
        )
        return response.is_temp_reserved

    async def _confirm_reserve(self, flight_id, seats_amount):
        airline_stub = self.airline_flights[flight_id]
        response = await airline_stub.ConfirmReserve(
            airline_service_pb2.ReserveRequest(flight_id=flight_id, seats_amount=seats_amount)
        )
        return response.is_reserved

class TicketServiceServer:
    """
    Represents the server that hosts the TicketService gRPC service.
    """

    def __init__(self, port, airline_addresses):
        """
        Initialize the TicketServiceServer.

        :param port: The port number the server will listen on.
        :param airline_addresses: A dictionary mapping airline names to their gRPC server addresses.
        """
        self.port = port
        self.airline_addresses = airline_addresses
        self.server = grpc.aio.server()

    async def start(self):
        """
        Start the gRPC server, register the TicketService, and begin listening for requests.
        """
        logging.basicConfig()
        add_TicketServiceServicer_to_server(TicketServiceServicer(self.airline_addresses), self.server)
        self.server.add_insecure_port(f"[::]:{self.port}")
        await self.server.start()
        print(f"Server started, listening on {self.port}")
        await self.server.wait_for_termination()
