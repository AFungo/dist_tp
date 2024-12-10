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
        self.airline_flights = {}


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
                    self.airline_flights[int(f_id)] =  airline
                    f = Flight(f_id, f_data["src"], f_data["dest"])
                    f.set_seats_status(f_data["seats"]) 
                    flights.append(f)

        flight_package = self.ticket_service.get_flights(flights, request.src, request.dest)
        paths = [[flight.to_dict() for flight in package] for package in flight_package]
        return FlightsByRouteReply(flights=json.dumps(paths))

    def BuyFlightPackage(self, request, context):
        for i in range(len(request.flights_id)):
            id = request.flights_id[i]
            seat = request.seat_numbers[i]
            # Aca deberiamos hacer como la reserva de tres pasos?
            response = self.airline_flights[id].Reserve(airline_service_pb2.ReserveRequest(flight_id=id, seat_number=seat))
            #chequeamos que el response este habilitado, es decir esta reservado
            #luego mandamos una request con confirmar la reserva por lo que ailine lo cambia a ocupado
            #esta oficialmente comprado
            #en el caso que fallo la reserva en la primera request se hace el camino de informarle 
            # al usuario de que la compra no se pudo realizar
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
