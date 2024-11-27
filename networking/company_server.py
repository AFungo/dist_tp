import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from concurrent import futures
import logging

import grpc
from classes.airport import Airport
from classes.company import Company
from classes.flight import Flight
import ticket_purchase_pb2
import ticket_purchase_pb2_grpc


class TicketPurchase(ticket_purchase_pb2_grpc.TicketPurchaseServicer):
    def __init__(self, company):
        self.company = company

    def GetFreeSeats(self, request, context):
        return ticket_purchase_pb2.FreeSeatReply(message=str(self.company.get_free_seats(0)))


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    company = Company("Splinter")
    company.add_flight(Flight(Airport.RCU, Airport.EZE, 2))
    ticket_purchase_pb2_grpc.add_TicketPurchaseServicer_to_server(TicketPurchase(company), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()