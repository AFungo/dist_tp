import json

from argparse import ArgumentParser
from classes.airline import Airline
from classes.flight import Flight
from networking.airline_server import AirlineServer
    

def create(filename):
    filename = "resources/" + filename
    with open(filename, 'r') as f:
        data = json.load(f)
        
    flights = []
    for f in data["flights"]:   
        flights.append(Flight(f["id"], f["src"], f["dest"], f["seats_available"])) #Se va a romper acá
        
    company = Airline(data["name"], flights)
    company_server = AirlineServer(company, data["port"])
    return company, company_server


def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", dest="input")
    args = parser.parse_args()
    company, company_server = create(args.input)
    company_server.start()
    

if __name__ == "__main__":
    main()    