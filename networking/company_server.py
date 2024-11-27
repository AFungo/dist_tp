from concurrent import futures
import logging

import grpc
import ticket_purchase_pb2
import ticket_purchase_pb2_grpc


class TicketPurchase(ticket_purchase_pb2_grpc.TicketPurchaseServicer):
    def GetFreeSeats(self, request, context):
        return ticket_purchase_pb2.FreeSeatReply(message=" Hola Valen ")


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ticket_purchase_pb2_grpc.add_TicketPurchaseServicer_to_server(TicketPurchase(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()