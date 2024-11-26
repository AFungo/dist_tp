from enum import Enum

global_id = 0
class SeatStatus(Enum):
    FREE = 1
    TEMPORARY_RESERVED = 2
    RESERVED = 3
SeatStatus = Enum('SeatStatus', [('FREE', 1), ('TEMPORARY_RESERVED', 2), ('RESERVED', 3)])

class Flight:
    def __init__(self, source, dest, seats_amount):
        global global_id
        self.id = global_id
        global_id += 1
        self.source = source
        self.dest = dest
        self.seats = [SeatStatus.FREE] * seats_amount

    def is_free(self, seat_number):
        return self.seats[seat_number] == SeatStatus.FREE

    def is_reserved(self, seat_number):
        return self.seats[seat_number] == SeatStatus.RESERVED
    
    def is_temporary_reserved(self, seat_number):
        return self.seats[seat_number] == SeatStatus.TEMPORARY_RESERVED
    
    def reserve_seat(self, seat_number):
        self.seats[seat_number] = SeatStatus.RESERVED
        
    def temporary_reserve_seat(self, seat_number):
        self.seats[seat_number] = SeatStatus.TEMPORARY_RESERVED
        
    def free_seat(self, seat_number):
        self.seats[seat_number] = SeatStatus.FREE
    