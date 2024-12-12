import json
import logging
import grpc

from classes.flight import Flight
from classes.ticket_service import TicketService
from networking.airline import airline_service_pb2
from networking.airline.airline_service_pb2_grpc import AirlineServiceStub

from networking.ticket_service.ticket_service_pb2 import BuyFlightPackageReply, FlightsByRouteReply
from networking.ticket_service.ticket_service_pb2_grpc import TicketServiceServicer, add_TicketServiceServicer_to_server
from concurrent import futures

class TicketServiceServicer(TicketServiceServicer):
    """
    Implements the TicketService gRPC service to manage ticket-related operations.
    """
    
    def __init__(self, airline_addresses):
        """
        Initializes the TicketServiceServicer with the given airline addresses.

        :param airline_addresses: A dictionary mapping airline names to their gRPC server addresses.
        """

        self.ticket_service = TicketService() # Service for ticket-related business logic.
        self.airline_clients = [] # List of AirlineServiceStub clients for gRPC communication.
        self.airline_flights = {} # Maps flight IDs to their respective airline clients.

        # Create a gRPC channel and stub for each airline address.
        for address in airline_addresses.values():
            channel = grpc.insecure_channel(address)
            self.airline_clients.append(AirlineServiceStub(channel))

    def GetFlightsByRoute(self, request, context):
        """
        Handles the gRPC request to get all flight packages available for a given route.
        """
        flights = []
        # Retrieve flights from all airline clients.
        for airline in self.airline_clients:
            response = airline.GetAllFlights(airline_service_pb2.AllFlightsRequest())
            airline_flights = json.loads(response.all_flights)
            # Process each flight and map it to the corresponding airline.
            for f_data in airline_flights:
                self.airline_flights[f_data["id"]] = airline
                flights.append(f_data)

        # Use TicketService to find flight packages matching the source and destination.
        flight_package = self.ticket_service.get_flights(flights, request.src, request.dest)
        return FlightsByRouteReply(flights=json.dumps(flight_package))


    def BuyFlightPackage(self, request, context):
        """
        Handles the gRPC request to buy a flight package (multiple flights).
        """
        seats_amount = request.seats_amount

        for id in request.flights_id:
            airline_stub = self.airline_flights[id]

            response = airline_stub.Reserve(
                airline_service_pb2.ReserveRequest(flight_id=id, seats_amount=seats_amount)
            )

            if not response.is_temp_reserved:
                # manejo de error
                return BuyFlightPackageReply(buy_success=False, message="ERROR")

        for id in request.flights_id:        
            response = airline_stub.ConfirmReserve(
                airline_service_pb2.ReserveRequest(flight_id=id, seats_amount=seats_amount)
            )
            if not response.is_reserved:
                # manejo de error
                return BuyFlightPackageReply(buy_success=False, message="ERROR")
        
        return BuyFlightPackageReply()

            # TODO: Check the response to ensure the seat was successfully reserved.
            # If successful, proceed to confirm the reservation.
            # If reservation fails, inform the user and handle rollback.

            # Step 2: Confirm the reservation, officially marking the seat as purchased.
            # This step should only be executed if the reservation was successful.
            # TODO: Add the confirm logic here.

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
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        
    def start(self):
        """
        Start the gRPC server, register the TicketService, and begin listening for requests.
        """
        logging.basicConfig()
        add_TicketServiceServicer_to_server(TicketServiceServicer(self.airline_addresses), self.server)
        self.server.add_insecure_port("[::]:" + self.port)
        self.server.start()
        print("Server started, listening on " + self.port)
        self.server.wait_for_termination()    
