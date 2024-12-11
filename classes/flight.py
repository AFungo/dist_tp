class Flight:
    def __init__(self, flight_id: int, src: str, dest: str, seats_amount: int = 1):
        if seats_amount <= 0:
            raise ValueError("The number of seats must be greater than 0.")
        
        self.id = flight_id
        self.src = src
        self.dest = dest
        self.seats_available = seats_amount

    def are_seats_available(self, seats_amount):
        return self.seats_available >= seats_amount

    def get_seats_available(self):
        return self.seats_available

    def reserve_seats(self, seats_amount: int) -> None:
        self._validate_seats_amount(seats_amount)
        self.seats_available -= seats_amount

    def temporary_reserve_seat(self, seats_amount: int) -> None:
        self._validate_seats_amount(seats_amount)
        # Maybe append reservations in a buffer.
        self.seats_available -= seats_amount
        
    def free_seats(self, seats_amount: int) -> None:
        self.seats_available += seats_amount
    
    def to_dict(self):
        return {
            self.id : {    
                "src" : self.src,
                "dest" : self.dest,
                "seats" : self.seats_available
            }
        }

    def __repr__(self) -> str:
        return f"<Flight {self.id}: {self.src} -> {self.dest}, Seats: {self.seats_available}>"

    def _validate_seats_amount(self, seats_amount: int) -> None:
        if not (0 <= seats_amount < self.seats_available):
            raise ValueError(f"Invalid seat number: {seats_amount}")
    
    def is_temporary_reserved(self, seats_amount: int) -> bool:
        #TODO: See what to do with this method.
        pass