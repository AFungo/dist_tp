from __future__ import print_function

import logging

import grpc
import airline_service_pb2
import airline_service_pb2_grpc


def run():
    print("Will try to get free seats ...")
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = airline_service_pb2_grpc.AirlineServiceStub(channel)
        response = stub.GetFreeSeats(airline_service_pb2.FreeSeatRequest())
    print("Free seats: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()