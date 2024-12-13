import json
import logging
import grpc

from networking.airline.airline_service_pb2 import AllFlightsReply, ReserveReply, ConfirmReserveReply, CancelReserveReply, SeatsAvailableReply
from networking.airline.airline_service_pb2_grpc import AirlineServiceServicer, add_AirlineServiceServicer_to_server

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

    async def GetAllFlights(self, request, context):
        """
        Handles the gRPC request to retrieve all flights in the airline.
        """
        flights = self.airline.get_all_flights()
        flights = [f.to_dict() for f in flights.values()]
        return AllFlightsReply(all_flights=json.dumps(flights))

    async def GetSeatsAvailable(self, request, context):
        return SeatsAvailableReply(message=str(self.airline.get_seats_available(request.flight_id)))          

    async def Reserve(self, request, context):
        is_temp_reserved = self.airline.reserve(request.flight_id, request.seats_amount)
        return ReserveReply(is_temp_reserved=is_temp_reserved)
    
    async def ConfirmReserve(self, request, context):
        is_reserved = self.airline.confirm_reserve(request.flight_id, request.seats_amount)
        return ConfirmReserveReply(is_reserved=is_reserved)
    
    async def CancelReserve(self, request, context):
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
        self.server = grpc.aio.server()

    async def start(self):
        """
        Start the gRPC server, register the AirlineService, and begin listening for requests.
        """
        logging.basicConfig()
        add_AirlineServiceServicer_to_server(AirlineService(self.airline), self.server)
        self.server.add_insecure_port("[::]:" + self.port)
        await self.server.start()
        print("Server started, listening on " + self.port)
        await self.server.wait_for_termination()
        