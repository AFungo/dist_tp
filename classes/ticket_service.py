class TicketService:
    def __init__(self, airlines=[]):
        self.airlines = airlines
        
    def get_flights_by_src(self, src):
        return [f for a in self.airlines for f in a.flights if f.src == src]
    
    def get_flights(self, src, dest):
        stack = [(src, [])]
        paths = []
        while stack:
            current, path = stack.pop()

            if current == dest:
                paths.append(path)
                continue

            for flight in self.get_flights_by_src(current):
                if flight.dest not in [f.src for f in path]:
                    stack.append((flight.dest, path + [flight]))
                
        return paths   
    
    def get_all_seats(self, flight_id):
        return [f for a in self.airlines for f in a.get_all_seats(flight_id)]
    
    def buy_ticket(self, flight_id, seat_number):
        for a in self.airlines:
            f = a.get_flight(flight_id)
            if not f is None:
                break
            
        f.reserve_seat(seat_number)