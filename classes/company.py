class Company:
    
    def __init__(self, name):
        self.name = name
        self.flights = []

    def get_flight(self, source, dest):
        for flight in self.flights:
            if flight.source == source and flight.dest == dest:
                return flight.id
        return None

    def get_flight_by_id(self, service_id):
        for f in self.flights:
            if f.id == service_id:
                return f
        return None

    def get_free_seats(self, service_id):
        flight = self.get_flight_by_id(service_id)
        if flight != None:
            free_seats = []
            for i in range(len(flight.seats)):
                if flight.is_free_seat(i):
                    free_seats.append(i)
            return free_seats
        return None
    
    def reserve(self, service_id, seat_number):
        flight = self.get_flight_by_id(service_id)
        if flight.is_free_seat(seat_number):
            flight.take_seat(seat_number)

    def confirm_reserve(self, service_id, seat_number):
        return 0

    def cancel_reserve(self, service_id, seat_number):
        flight = self.get_flight_by_id(service_id)
        if not flight.is_free_seat(seat_number):
            flight.drop_seat(seat_number)