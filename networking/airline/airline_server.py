import json
import logging
import grpc

from networking.airline.airline_service_pb2 import FreeSeatReply, AllFlightsReply, ReserveReply, ConfirmReserveReply, CancelReserveReply, AllSeatsReply
from networking.airline.airline_service_pb2_grpc import AirlineServiceServicer, add_AirlineServiceServicer_to_server
from concurrent import futures

class AirlineService(AirlineServiceServicer):
    """
    Implements the AirlineService gRPC service to manage airline-related operations.
    """

    def __init__(self, airline):
        """
        Initialize the AirlineService with the given airline.

        :param airline: An Airline object containing the flight and seat data.
        """
        self.airline = airline

    def GetFreeSeats(self, request, context):
        """
        Handles the gRPC request to retrieve the number of free seats for a flight.
        """        
        return FreeSeatReply(message=str(self.airline.get_free_seats(request.flight_id)))

    def GetAllFlights(self, request, context):
        """
        Handles the gRPC request to retrieve all flights in the airline.
        """
        flights = self.airline.get_all_flights()
        flights = [f.to_dict() for f in flights.values()]
        return AllFlightsReply(all_flights=json.dumps(flights))

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
    """
    Represents the server that hosts the AirlineService gRPC service.
    """
    def __init__(self, airline, port):
        """
        Initialize the AirlineServer.

        :param airline: An Airline object containing the flight and seat data.
        :param port: The port number the server will listen on.
        """
        self.airline = airline
        self.port = port
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    def start(self):
        """
        Start the gRPC server, register the AirlineService, and begin listening for requests.
        """
        logging.basicConfig()
        add_AirlineServiceServicer_to_server(AirlineService(self.airline), self.server)
        self.server.add_insecure_port("[::]:" + self.port)
        self.server.start()
        print("Server started, listening on " + self.port)
        self.server.wait_for_termination()
        