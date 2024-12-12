class Flight:
    def __init__(self, flight_id: int, src: str, dest: str, seats_amount: int = 1):
        if seats_amount <= 0:
            raise ValueError("The number of seats must be greater than 0.")
        
        self.id = flight_id
        self.src = src
        self.dest = dest
        self.seats_available = seats_amount
        self.temporary_reserved_seats = 0

    def are_seats_available(self, seats_amount):
        """
        If there are enough seats available contemplating the difference between the reserved and available seats
        """
        return self.seats_available - self.temporary_reserved_seats >= seats_amount
    
    def are_effectively_seats_available(self, seats_amount):
        """
        If there are enough temporary reserved seats
        """
        return self.seats_available >= seats_amount and seats_amount <= self.temporary_reserved_seats 

    def get_seats_available(self):
        return self.seats_available - self.temporary_reserved_seats

    def reserve_seats(self, seats_amount: int) -> None:
        if self.are_effectively_seats_available(seats_amount):
            self.temporary_reserved_seats -= seats_amount
            self.seats_available -= seats_amount
            return True
        return False

    def temporary_reserve_seats(self, seats_amount: int) -> None:
        if self.are_seats_available(seats_amount):
            self.temporary_reserved_seats += seats_amount
            return True 
        return False
        
    def free_seats(self, seats_amount: int) -> None:
        if (self.temporary_reserved_seats - seats_amount) >= 0:
            self.temporary_reserved_seats -= seats_amount
            return True
        return False
    
    def to_dict(self):
        return {
            self.id : {    
                "src" : self.src,
                "dest" : self.dest,
                "seats" : self.get_seats_available()
            }
        }

    def __repr__(self) -> str:
        return f"<Flight {self.id}: {self.src} -> {self.dest}, Seats: {self.seats_available}>"