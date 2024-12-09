import json
import logging
import grpc

from classes.flight import Flight
from classes.ticket_service import TicketService
from networking.airline import airline_service_pb2
from networking.airline.airline_service_pb2_grpc import AirlineServiceStub

from classes.airport import Airport

from networking.ticket_service.ticket_service_pb2 import BuyFlightPackageReply, FlightsByRouteReply
from networking.ticket_service.ticket_service_pb2_grpc import TicketServiceServicer, add_TicketServiceServicer_to_server
from concurrent import futures

class TicketServiceServicer(TicketServiceServicer):
    def __init__(self, airline_addresses):
        self.ticket_service = TicketService()
        self.airline_clients = []
        
        for address in airline_addresses.values():
            channel = grpc.insecure_channel(address)
            self.airline_clients.append(AirlineServiceStub(channel))
    
    def GetFlightsByRoute(self, request, context):
        flights = []
        for airline in self.airline_clients:
            response = airline.GetAllFlights(airline_service_pb2.AllFlightsRequest())
            airline_flights = json.loads(response.all_flights)
            
            for flight in airline_flights:
                for f_id, f_data in flight.items():
                    flights.append(Flight(f_id, f_data["src"], f_data["dest"], seats=f_data["seats"]))
            
        flight_package = self.ticket_service.get_flights(flights, request.src, request.dest)
        paths = [[flight.to_dict() for flight in package] for package in flight_package]
        return FlightsByRouteReply(flights=json.dumps(paths))

    def BuyFlightPackage(self, request, context):
        for id in request.flights_id:
            
            
        self.ticket_service.buy_ticket(request.flights_id[0], request.seat_numbers[0])
        self.ticket_service.buy_ticket(request.flights_id[1], request.seat_numbers[1])
        return BuyFlightPackageReply()

class TicketServiceServer:
    def __init__(self, ticket_service, port, airline_addresses):
        #self.ticket_service = ticket_service
        self.port = port
        self.airline_addresses = airline_addresses
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        
    def start(self):
        logging.basicConfig()
        add_TicketServiceServicer_to_server(TicketServiceServicer(self.airline_addresses), self.server)
        self.server.add_insecure_port("[::]:" + self.port)
        self.server.start()
        print("Server started, listening on " + self.port)
        self.server.wait_for_termination()    
