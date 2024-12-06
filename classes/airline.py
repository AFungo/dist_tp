class Airline:
    
    def __init__(self, name, flights={}):
        self.name = name
        self.flights = flights

    def get_all_flights(self):
        return self.flights

    def get_flight(self, flight_id):
        return self.flights[flight_id]

    def get_free_seats(self, flight_id):
        return self.flights[flight_id].get_free_seats()
        
    def reserve(self, flight_id, seat_number):
        flight = self.get_flight(flight_id)
        if flight.is_free(seat_number):
            flight.temporary_reserve_seat(seat_number)

    def confirm_reserve(self, flight_id, seat_number):
        flight = self.get_flight(flight_id)
        if flight.is_temporary_reserved(seat_number):
            flight.reserve_seat(seat_number)

    def cancel_reserve(self, flight_id, seat_number):
        flight = self.get_flight(flight_id)
        if flight.is_temporary_reserved(seat_number):
            flight.free_seat(seat_number)

    def get_all_seats(self, flight_id):
        return self.flight[flight_id].get_seats()        
    
    
    def to_dict(self):
        d = {}
        d["name"] = self.name       
        for flight in self.flights.values():
            d.update(flight.to_dict())
            
        return d
    