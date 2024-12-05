import logging
import sys
from pathlib import Path
# Add the root directory to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from classes.airline import Airline
from classes.airport import Airport
from classes.flight import Flight


import grpc
from networking.ticket_service_pb2 import BuyFlightPackageReply, FlightsByRouteReply
from networking.ticket_service_pb2_grpc import TicketServiceServicer, add_TicketServiceServicer_to_server
from concurrent import futures

from classes.ticket_service import TicketService

class TicketServiceServicer(TicketServiceServicer):
    def __init__(self):
        company = Airline("Aerolineas Argentina")
        company.flights.append(Flight(1, Airport.RCU, Airport.EZE, 2))
        company.flights.append(Flight(2, Airport.EZE, Airport.RCU, 2))
        company.flights.append(Flight(3, Airport.EZE, Airport.AEP, 2))
        company.flights.append(Flight(4, Airport.AEP, Airport.EZE, 2))
        company.flights.append(Flight(5, Airport.RCU, Airport.GDZ, 2))
        company.flights.append(Flight(6, Airport.GDZ, Airport.RCU, 2))
        company.flights.append(Flight(7, Airport.GDZ, Airport.AEP, 2))
        company.flights.append(Flight(8, Airport.AEP, Airport.GDZ, 2))
        company.flights.append(Flight(9, Airport.GDZ, Airport.EZE, 2))
        company.flights.append(Flight(10, Airport.EZE, Airport.GDZ, 2))
        self.ticket_service = TicketService([company])
    
    def GetFlightsByRoute(self, request, context):
        f = self.ticket_service.get_flights(Airport(request.src), Airport(request.dest))
        return FlightsByRouteReply(flights=str(f)) 

    def BuyFlightPackage(self, request, context):
        self.ticket_service.buy_ticket(request.flights_id[0], request.seat_numbers[0])
        self.ticket_service.buy_ticket(request.flights_id[1], request.seat_numbers[1])
        return BuyFlightPackageReply()


def start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_TicketServiceServicer_to_server(TicketServiceServicer(), server)
    server.add_insecure_port("[::]:" + '8001')
    server.start()
    print("Server started, listening on " + '8001')
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()

    start()