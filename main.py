
from classes.company import Company
from classes.flight import Flight
from classes.airport import Airport

def main():
    company = Company("Aerolineas Argentina")
    company.flights.append(Flight(Airport.RCU, Airport.EZE, 2))
    company.flights.append(Flight(Airport.EZE, Airport.RCU, 2))
    
    company.flights.append(Flight(Airport.EZE, Airport.AEP, 2))
    company.flights.append(Flight(Airport.AEP, Airport.EZE, 2))
    
    company.flights.append(Flight(Airport.RCU, Airport.GDZ, 2))
    company.flights.append(Flight(Airport.GDZ, Airport.RCU, 2))
    
    company.flights.append(Flight(Airport.GDZ, Airport.AEP, 2))
    company.flights.append(Flight(Airport.AEP, Airport.GDZ, 2))
    
    company.flights.append(Flight(Airport.GDZ, Airport.EZE, 2))
    company.flights.append(Flight(Airport.EZE, Airport.GDZ, 2))
    
    print(company.find_all_paths(Airport.RCU, Airport.AEP))
    

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