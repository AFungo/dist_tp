from __future__ import print_function

import logging

import grpc
import airline_service_pb2
import airline_service_pb2_grpc
import ticket_service_pb2
import ticket_service_pb2_grpc

def run():
    print("Will try to get free seats ...")
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = airline_service_pb2_grpc.AirlineServiceStub(channel)
        response = stub.GetAllFlights(airline_service_pb2.AllFlightsRequest())
        response = stub.GetAllSeats(airline_service_pb2.FreeSeatRequest(flight_id=1))
        print("Seats: " + response.message)
        stub.Reserve(airline_service_pb2.ReserveRequest(flight_id=1, seat_number=1))
        response = stub.GetAllSeats(airline_service_pb2.FreeSeatRequest(flight_id=1))
        print("Seats: " + response.message)
        stub.ConfirmReserve(airline_service_pb2.ConfirmReserveRequest(flight_id=1, seat_number=1))
        response = stub.GetAllSeats(airline_service_pb2.FreeSeatRequest(flight_id=1))
        print("Seats: " + response.message)
        stub.CancelReserve(airline_service_pb2.CancelReserveRequest(flight_id=1, seat_number=1))
        response = stub.GetAllSeats(airline_service_pb2.FreeSeatRequest(flight_id=1))
        print("Seats: " + response.message)

def run_ticket_buyer():
    print("Will try to buy a ticket package ...")
    with grpc.insecure_channel("localhost:8001") as channel:
        stub = ticket_service_pb2_grpc.TicketServiceStub(channel)
        response = stub.GetFlightsByRoute(ticket_service_pb2.FlightsByRouteRequest(src="RCU", dest="AEP"))
        stub.BuyFlightPackage(ticket_service_pb2.BuyFlightPackageRequest(flights_id=[5, 7], seat_numbers=[1,1]))
        r = response.flights.split('[')
        for a in r:
            print(a)

if __name__ == "__main__":
    logging.basicConfig()
    # run()
    run_ticket_buyer()