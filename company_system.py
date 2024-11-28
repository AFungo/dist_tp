import json

from argparse import ArgumentParser
from classes.company import Company
from classes.flight import Flight
from networking.company_server import CompanyServer
    

def create(filename):
    filename = "resources/" + filename
    with open(filename, 'r') as f:
        data = json.load(f)
        
    flights = []
    for f in data["flights"]:   
        flights.append(Flight(f["src"], f["dest"], f["seats_available"])) #Se va a romper acá
        
    company = Company(data["name"], flights)
    company_server = CompanyServer(company, data["port"])
    return company, company_server


def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", dest="input")
    args = parser.parse_args()
    company, company_server = create(args.input)
    company_server.start()
    

if __name__ == "__main__":
    main()    