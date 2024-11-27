from __future__ import print_function

import logging

import grpc
import ticket_purchase_pb2
import ticket_purchase_pb2_grpc


def run():
    print("Will try to get free seats ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = ticket_purchase_pb2_grpc.TicketPurchaseStub(channel)
        response = stub.GetFreeSeats(ticket_purchase_pb2.FreeSeatRequest())
    print("Free seats: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()