import json
import os

from classes.airline import Airline
from classes.flight import Flight
from networking.airline.airline_server import AirlineServer
from networking.ticket_service.ticket_service_server import TicketServiceServer

class ConfigLoader:
    def __init__(self):
        from argparse import ArgumentParser
        self.parser = ArgumentParser()
        self.parser.add_argument("-i", "--input", dest="input")
        self.parser.add_argument("-a", "--address", dest="address", required=False, default="localhost:8001")
        self.args = self.parser.parse_args()
        
    def load_config_file(self):
        file_path = self.args.input
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Configuration file '{file_path}' not found.")
        with open(file_path, 'r') as f:
            return json.load(f)

    def create_airline_server(self):
        data = self.load_config_file()
        flights = {
            f["id"]: Flight(f["id"], f["src"], f["dest"], data["name"], f["seats_available"])
            for f in data["flights"]
        }
        airline = Airline(data["name"], flights)
        server = AirlineServer(airline, data["port"])
        return airline, server

    def create_ticket_service_server(self): 
        data = self.load_config_file()
        server = TicketServiceServer(data["port"], data["airline_addresses"], data["neighbor_addresses"], data["id"])
        return server 
    
    def get_address(self):
        return self.args.address
        