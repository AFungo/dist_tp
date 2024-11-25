
global_id = 0

class Flight:

    def __init__(self, source, dest, seats_amount):
        global global_id
        #date = 0 #es necesario?
        self.id = global_id
        global_id += 1
        self.source = source
        self.dest = dest
        self.seats = [0] * seats_amount

    def is_free_seat(self, seat_number):
        return self.seats[seat_number] == 0

    def take_seat(self, seat_number):
        self.seats[seat_number] = 1
    
    def drop_seat(self, seat_number):
        self.seats[seat_number] = 0
