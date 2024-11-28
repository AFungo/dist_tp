import sys
from pathlib import Path

# Add the root directory to sys.path
sys.path.insert(0, str(Path(__file__).parent))

import grpc
from networking.ticket_purchase_pb2 import FreeSeatReply
from networking.ticket_purchase_pb2_grpc import TicketPurchaseServicer, add_TicketPurchaseServicer_to_server
from concurrent import futures

class TicketPurchase(TicketPurchaseServicer):
    def __init__(self, company):
        self.company = company

    def GetFreeSeats(self, request, context):
        return FreeSeatReply(message=str(self.company.get_free_seats(0)))


class CompanyServer:
    def __init__(self, company, port):
        self.company = company
        self.port = port
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    def start(self):
        add_TicketPurchaseServicer_to_server(TicketPurchase(self.company), self.server)
        self.server.add_insecure_port("[::]:" + self.port)
        self.server.start()
        print("Server started, listening on " + self.port)
        self.server.wait_for_termination()
        