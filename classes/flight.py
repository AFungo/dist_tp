from enum import Enum
from typing import List, Dict


class SeatStatus(Enum):
    FREE = 1
    TEMPORARY_RESERVED = 2
    RESERVED = 3


class Flight:
    def __init__(self, flight_id: int, src: str, dest: str, seats_amount: int = 1):
        if seats_amount <= 0:
            raise ValueError("The number of seats must be greater than 0.")
        
        self.id = flight_id
        self.src = src
        self.dest = dest
        self.seats = [SeatStatus.FREE] * seats_amount

    def check_seat_status(self, seat_number: int, status: SeatStatus) -> bool:
        self._validate_seat_number(seat_number)
        return self.seats[seat_number] == status

    def change_seat_status(self, seat_number: int, new_status: SeatStatus) -> None:
        self._validate_seat_number(seat_number)
        self.seats[seat_number] = new_status

    def get_free_seats(self) -> List[int]:
        return [i for i, status in enumerate(self.seats) if status == SeatStatus.FREE]

    def to_dict(self):
        return {
            self.id : {    
                "src" : self.src,
                "dest" : self.dest,
                "seats" : [status for status in self.seats]
            }
        }

    def __repr__(self) -> str:
        return f"<Flight {self.id}: {self.src} -> {self.dest}, Seats: {self.seats}>"

    def _validate_seat_number(self, seat_number: int) -> None:
        if not (0 <= seat_number < len(self.seats)):
            raise ValueError(f"Invalid seat number: {seat_number}")

    def is_free(self, seat_number: int) -> bool:
        return self.check_seat_status(seat_number, SeatStatus.FREE)

    def is_reserved(self, seat_number: int) -> bool:
        return self.check_seat_status(seat_number, SeatStatus.RESERVED)

    def is_temporary_reserved(self, seat_number: int) -> bool:
        return self.check_seat_status(seat_number, SeatStatus.TEMPORARY_RESERVED)

    def reserve_seat(self, seat_number: int) -> None:
        self.change_seat_status(seat_number, SeatStatus.RESERVED)

    def temporary_reserve_seat(self, seat_number: int) -> None:
        self.change_seat_status(seat_number, SeatStatus.TEMPORARY_RESERVED)

    def free_seat(self, seat_number: int) -> None:
        self.change_seat_status(seat_number, SeatStatus.FREE)