from enum import Enum

class SeatStatus(Enum):
    FREE = 1
    TEMPORARY_RESERVED = 2
    RESERVED = 3

class Flight:
    def __init__(self, id, src, dest, seats_amount):
        self.id = id
        self.src = src
        self.dest = dest
        self.seats = [SeatStatus.FREE.value] * seats_amount

    def is_free(self, seat_number):
        self._validate_seat_number(seat_number)
        return self.seats[seat_number] == SeatStatus.FREE

    def is_reserved(self, seat_number):
        self._validate_seat_number(seat_number)
        return self.seats[seat_number] == SeatStatus.RESERVED
    
    def is_temporary_reserved(self, seat_number):
        self._validate_seat_number(seat_number)
        return self.seats[seat_number] == SeatStatus.TEMPORARY_RESERVED
    
    def reserve_seat(self, seat_number):
        self._validate_seat_number(seat_number)
        self.seats[seat_number] = SeatStatus.RESERVED.value
        
    def temporary_reserve_seat(self, seat_number):
        self._validate_seat_number(seat_number)
        self.seats[seat_number] = SeatStatus.TEMPORARY_RESERVED.value
        
    def free_seat(self, seat_number):
        self._validate_seat_number(seat_number)
        self.seats[seat_number] = SeatStatus.FREE.value
    
    def get_seats(self):
        return self.seats

    def get_free_seats(self):
        return [i for i in range(len(self.seats)) if self.is_free(i)]
    
    def _validate_seat_number(self, seat_number):
        if seat_number < 0 or seat_number >= len(self.seats):
            raise ValueError(f"Invalid seat number: {seat_number}")

    def __repr__(self):
        string = f"<{self.id}, {self.src}, {self.dest}>"
        return string
    
    def to_dict(self):
        return {
            self.id : {    
                "src" : self.src,
                "dest" : self.dest,
                "seats" : self.seats
            }
        }