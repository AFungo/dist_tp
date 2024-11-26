
from classes.company import Company
from classes.flight import Flight
from classes.airport import Airport

def main():
    company = Company("Aerolineas Argentina")
    company.flights.append(Flight(Airport.RCU, Airport.EZE, 2))

    flight_id = company.get_flight(Airport.RCU, Airport.EZE)
    print("Flight_id ", flight_id)
    seats_number = company.get_free_seats(flight_id)
    print("Seats ", seats_number)
    company.reserve(flight_id, seats_number[0])
    seats_number = company.get_free_seats(flight_id)
    print("Seats", seats_number)
    company.reserve(flight_id, seats_number[0])
    seats_number = company.get_free_seats(flight_id)
    print("Seats ", seats_number)
    company.cancel_reserve(flight_id, 0)
    seats_number = company.get_free_seats(flight_id)
    print("Seats ",seats_number)

if __name__ == "__main__":
    main()