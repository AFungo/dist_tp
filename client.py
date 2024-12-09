import json
import logging
import grpc
import networking

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent) + "/networking/airline")
sys.path.insert(0, str(Path(__file__).parent) + "/networking/ticket_service")


from classes.config_loader import ConfigLoader

""" def run():
    print("Will try to get free seats ...")
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = networking.airline.airline_service_pb2_grpc.AirlineServiceStub(channel)
        response = stub.GetAllFlights(networking.airline.airline_service_pb2.AllFlightsRequest())
        response = stub.GetAllSeats(networking.airline.airline_service_pb2.FreeSeatRequest(flight_id=1))
        print("Seats: " + response.message)
        stub.Reserve(networking.airline.airline_service_pb2.ReserveRequest(flight_id=1, seat_number=1))
        response = stub.GetAllSeats(networking.airline.airline_service_pb2.FreeSeatRequest(flight_id=1))
        print("Seats: " + response.message)
        stub.ConfirmReserve(networking.airline.airline_service_pb2.ConfirmReserveRequest(flight_id=1, seat_number=1))
        response = stub.GetAllSeats(networking.airline.airline_service_pb2.FreeSeatRequest(flight_id=1))
        print("Seats: " + response.message)
        stub.CancelReserve(networking.airline.airline_service_pb2.CancelReserveRequest(flight_id=1, seat_number=1))
        response = stub.GetAllSeats(networking.airline.airline_service_pb2.FreeSeatRequest(flight_id=1))
        print("Seats: " + response.message) """

# python3 client2.py -a localhost:8001
def main():
    config_loader = ConfigLoader()
    address = config_loader.get_address()
    with grpc.insecure_channel(address) as channel:
        stub = networking.ticket_service.ticket_service_pb2_grpc.TicketServiceStub(channel)
        response = stub.GetFlightsByRoute(networking.ticket_service.ticket_service_pb2.FlightsByRouteRequest(src="RCU", dest="AEP"))
        fs = json.loads(response.flights)
        for f in fs:
            print(f)
        
        stub.BuyFlightPackage(networking.ticket_service.ticket_service_pb2.BuyFlightPackageRequest(flights_id=[5, 7], seat_numbers=[1,1]))
        print()
        fs = json.loads(response.flights)
        for f in fs:
            print(f)
        
if __name__ == "__main__":
    logging.basicConfig()
    # run()
    main()