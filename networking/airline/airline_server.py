import json
import logging
import grpc

from networking.airline.airline_service_pb2 import FreeSeatReply, AllFlightsReply, ReserveReply, ConfirmReserveReply, CancelReserveReply, AllSeatsReply
from networking.airline.airline_service_pb2_grpc import AirlineServiceServicer, add_AirlineServiceServicer_to_server
from concurrent import futures

class AirlineService(AirlineServiceServicer):
    def __init__(self, airline):
        self.airline = airline

    def GetFreeSeats(self, request, context):
        return FreeSeatReply(message=str(self.airline.get_free_seats(request.flight_id)))

    def GetAllFlights(self, request, context):
        
        self.airline.to_dict()
        flights_json = json.dumps(self.airline.to_dict())
        
        return AllFlightsReply(all_flights=flights_json)

    def Reserve(self, request, context):
        self.airline.reserve(request.flight_id, request.seat_number)
        return ReserveReply()
    
    def ConfirmReserve(self, request, context):
        self.airline.confirm_reserve(request.flight_id, request.seat_number)
        return ConfirmReserveReply()
    
    def CancelReserve(self, request, context):
        self.airline.cancel_reserve(request.flight_id, request.seat_number)
        return CancelReserveReply()
    
    def GetAllSeats(self, request, context):
        return AllSeatsReply(message=str(self.airline.get_all_seats(request.flight_id)))          
    
class AirlineServer:
    def __init__(self, airline, port):
        self.airline = airline
        self.port = port
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    def start(self):
        logging.basicConfig()
        add_AirlineServiceServicer_to_server(AirlineService(self.airline), self.server)
        self.server.add_insecure_port("[::]:" + self.port)
        self.server.start()
        print("Server started, listening on " + self.port)
        self.server.wait_for_termination()
        