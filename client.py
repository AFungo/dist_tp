import asyncio
import json
import logging
import grpc
import networking
import random

import sys
from pathlib import Path

import networking.ticket_service
import networking.ticket_service.ticket_service_pb2

sys.path.insert(0, str(Path(__file__).parent) + "/networking/airline")
sys.path.insert(0, str(Path(__file__).parent) + "/networking/ticket_service")

from classes.config_loader import ConfigLoader

# python3 client2.py -a localhost:8001
async def main():
    config_loader = ConfigLoader()
    address = config_loader.get_address()
    async with grpc.aio.insecure_channel(address) as channel:
        stub = networking.ticket_service.ticket_service_pb2_grpc.TicketServiceStub(channel)
           
        # for i in range(0, 3):
        #     await buy_flight(stub, [12, 0, 28], 1)
            #num = random.randrange(0, 29, 3)
        
        # await get_flights_by_src_and_dest(stub, "SAO", "MAD")
        await get_all_flights(stub)
        

async def get_flights_by_src_and_dest(stub, src, dest):
    response = await stub.GetFlightsByRoute(networking.ticket_service.ticket_service_pb2.FlightsByRouteRequest(src=src, dest=dest))
    fs = json.loads(response.flights)
    for f in fs:
        print(f)

async def get_all_flights(stub):
    response = await stub.GetAllFlights(networking.ticket_service.ticket_service_pb2.TSAllFlightsRequest())
    fs = json.loads(response.all_flights)
    for flight in fs:
        print(flight)
        
async def buy_flight(stub, flights_id, seats_amount):
    response = await stub.BuyFlightPackage(networking.ticket_service.ticket_service_pb2.BuyFlightPackageRequest(flights_id=flights_id, seats_amount=seats_amount))
    if(not response.buy_success):
        print(response.message)
    else:  
        print(f"VUELOS {flights_id} COMPRADOS")
    
if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(main())
    
    
  