import json
import logging

from networking.airline import airline_service_pb2
from networking.airline.airline_service_pb2_grpc import AirlineServiceStub

from classes.airport import Airport


import grpc
from networking.ticket_service.ticket_service_pb2 import BuyFlightPackageReply, FlightsByRouteReply
from networking.ticket_service.ticket_service_pb2_grpc import TicketServiceServicer, add_TicketServiceServicer_to_server
from concurrent import futures


class TicketServiceServicer(TicketServiceServicer):
    def __init__(self, ticket_service, airline_addresses):
        self.ticket_service = ticket_service
        self.airline_clients = []
        for address in airline_addresses.values():
            channel = grpc.insecure_channel(address)
            self.airline_clients.append(AirlineServiceStub(channel))

    
    def GetFlightsByRoute(self, request, context):
        for airline in self.airline_clients:
            response = airline.GetAllFlights(airline_service_pb2.AllFlightsRequest())
        
        flights = json.loads(response.all_flights)
        print(flights)
        
        f = self.ticket_service.get_flights(flights, Airport(request.src), Airport(request.dest))
        return FlightsByRouteReply(flights=str(f))

    def BuyFlightPackage(self, request, context):
        self.ticket_service.buy_ticket(request.flights_id[0], request.seat_numbers[0])
        self.ticket_service.buy_ticket(request.flights_id[1], request.seat_numbers[1])
        return BuyFlightPackageReply()

class TicketServiceServer:
    def __init__(self, ticket_service, port, airline_addresses):
        self.ticket_service = ticket_service
        self.port = port
        self.airline_addresses = airline_addresses
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        
    def start(self):
        logging.basicConfig()
        add_TicketServiceServicer_to_server(TicketServiceServicer(self.ticket_service, self.airline_addresses), self.server)
        self.server.add_insecure_port("[::]:" + self.port)
        self.server.start()
        print("Server started, listening on " + self.port)
        self.server.wait_for_termination()    
