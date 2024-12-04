
from classes.airline import Airline
from classes.flight import Flight
from classes.ticket_service import TicketService
from classes.airport import Airport

def main():
    company = Airline("Aerolineas Argentina")
    
    company.flights.append(Flight(1, Airport.RCU, Airport.EZE, 2))
    company.flights.append(Flight(2, Airport.EZE, Airport.RCU, 2))
    
    company.flights.append(Flight(3, Airport.EZE, Airport.AEP, 2))
    company.flights.append(Flight(4, Airport.AEP, Airport.EZE, 2))
    
    company.flights.append(Flight(5, Airport.RCU, Airport.GDZ, 2))
    company.flights.append(Flight(6, Airport.GDZ, Airport.RCU, 2))
    
    company.flights.append(Flight(7, Airport.GDZ, Airport.AEP, 2))
    company.flights.append(Flight(8, Airport.AEP, Airport.GDZ, 2))
    
    company.flights.append(Flight(9, Airport.GDZ, Airport.EZE, 2))
    company.flights.append(Flight(10, Airport.EZE, Airport.GDZ, 2))
    
    ticket_service = TicketService([company])
    f = ticket_service.get_flights(Airport.RCU, Airport.AEP)
    
    for fl in f:
        print(fl)

    #flight_id = company.get_flight(Airport.RCU, Airport.EZE)
    #print("Flight_id ", flight_id)
    #seats_number = company.get_free_seats(flight_id)
    #print("Seats ", seats_number)
    #company.reserve(flight_id, seats_number[0])
    #seats_number = company.get_free_seats(flight_id)
    #print("Seats", seats_number)
    #company.reserve(flight_id, seats_number[0])
    #seats_number = company.get_free_seats(flight_id)
    #print("Seats ", seats_number)
    #company.cancel_reserve(flight_id, 0)
    #seats_number = company.get_free_seats(flight_id)
    #print("Seats ",seats_number)

if __name__ == "__main__":
    main()