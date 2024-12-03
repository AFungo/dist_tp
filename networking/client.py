from __future__ import print_function

import logging

import grpc
import airline_service_pb2
import airline_service_pb2_grpc


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

if __name__ == "__main__":
    logging.basicConfig()
    run()