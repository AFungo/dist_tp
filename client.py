import json
import logging
import grpc
import networking

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent) + "/networking/airline")
sys.path.insert(0, str(Path(__file__).parent) + "/networking/ticket_service")

from classes.config_loader import ConfigLoader

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
        
        stub.BuyFlightPackage(networking.ticket_service.ticket_service_pb2.BuyFlightPackageRequest(flights_id=[3, 5], seats_amount=[1, 1]))
        print()
    
        response = stub.GetFlightsByRoute(networking.ticket_service.ticket_service_pb2.FlightsByRouteRequest(src="RCU", dest="AEP"))
        fs = json.loads(response.flights)
        for f in fs:
            print(f)
        
if __name__ == "__main__":
    logging.basicConfig()
    main()