class Airline:
    
    def __init__(self, name, flights=[]):
        self.name = name
        self.flights = flights

    def get_all_flights(self):
        return self.flights

    def get_flight(self, src, dest):
        for flight in self.flights:
            if flight.src == src and flight.dest == dest:
                return flight.id
        return None

    def get_flight(self, flight_id):
        for f in self.flights:
            if f.id == flight_id:
                return f
        return None

    def get_free_seats(self, flight_id):
        return [f for f in self.get_flight(flight_id) if f.is_free()]
        
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
    
    def add_flight(self, flight):
        self.flights.append(flight)

    def get_all_seats(self, flight_id):
        f = self.get_flight(flight_id)
        return f.get_seats()        
