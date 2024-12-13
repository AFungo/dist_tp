import asyncio
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
async def main():
    config_loader = ConfigLoader()
    address = config_loader.get_address()
    async with grpc.aio.insecure_channel(address) as channel:
        stub = networking.ticket_service.ticket_service_pb2_grpc.TicketServiceStub(channel)
        
        tasks = []
        tasks.append(get_flights(stub, "RCU", "AEP"))
        tasks.append(buy_flight(stub, [1], 1))
        tasks.append(buy_flight(stub, [1], 1))
        tasks.append(buy_flight(stub, [2], 1))
        tasks.append(buy_flight(stub, [2], 1))
        tasks.append(buy_flight(stub, [3], 1))
        tasks.append(buy_flight(stub, [4], 1))
        tasks.append(buy_flight(stub, [5], 1))
        
        confirm_results = await asyncio.gather(*tasks)
        
        tasks = []
        tasks.append(get_flights(stub, "RCU", "AEP"))
        confirm_results = await asyncio.gather(*tasks)
        
        print("Ya terminaron de comprarse")
        
        
        
        
        
            
async def get_flights(stub, src, dest):
    response = await stub.GetFlightsByRoute(networking.ticket_service.ticket_service_pb2.FlightsByRouteRequest(src=src, dest=dest))
    fs = json.loads(response.flights)
    for f in fs:
        print(f)
        
async def buy_flight(stub, flights_id, seats_amount):
    response = await stub.BuyFlightPackage(networking.ticket_service.ticket_service_pb2.BuyFlightPackageRequest(flights_id=flights_id, seats_amount=seats_amount))
    if(not response.buy_success):
        print(response.message)
    print(f"VUELOS {flights_id} COMPRADOS")
    
if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(main())
    
    
  