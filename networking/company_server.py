import grpc
import ticket_purchase_pb2
import ticket_purchase_pb2_grpc
from concurrent import futures
        
class TicketPurchase(ticket_purchase_pb2_grpc.TicketPurchaseServicer):
    def __init__(self, company):
        self.company = company

    def GetFreeSeats(self, request, context):
        return ticket_purchase_pb2.FreeSeatReply(message=str(self.company.get_free_seats(0)))


class CompanyServer:
    def __init__(self, company, port):
        self.company = company
        self.port = port
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    def start(self):
        ticket_purchase_pb2_grpc.add_TicketPurchaseServicer_to_server(TicketPurchase(self.company), self.server)
        self.server.add_insecure_port("[::]:" + self.port)
        self.server.start()
        print("Server started, listening on " + self.port)
        self.server.wait_for_termination()
        