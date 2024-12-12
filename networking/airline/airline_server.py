import json
import logging
import grpc

from networking.airline.airline_service_pb2 import AllFlightsReply, ReserveReply, ConfirmReserveReply, CancelReserveReply, SeatsAvailableReply
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

    def GetAllFlights(self, request, context):
        """
        Handles the gRPC request to retrieve all flights in the airline.
        """
        flights = self.airline.get_all_flights()
        flights = [f.to_dict() for f in flights.values()]
        return AllFlightsReply(all_flights=json.dumps(flights))

    def GetSeatsAvailable(self, request, context):
        return SeatsAvailableReply(message=str(self.airline.get_seats_available(request.flight_id)))          

    def Reserve(self, request, context):
        self.airline.reserve(request.flight_id, request.seats_amount)
        return ReserveReply()
    
    def ConfirmReserve(self, request, context):
        self.airline.confirm_reserve(request.flight_id, request.seats_amount)
        return ConfirmReserveReply()
    
    def CancelReserve(self, request, context):
        self.airline.cancel_reserve(request.flight_id, request.seats_amount)
        return CancelReserveReply()
    
    
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
        