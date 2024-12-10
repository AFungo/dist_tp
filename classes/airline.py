class Airline:
    """
    Represents an airline that manages a collection of flights and seat reservations.
    """
    
    def __init__(self, name, flights={}):
        """
        Initialize an Airline instance.

        :param name: The name of the airline.
        :param flights: A dictionary mapping flight IDs to flight objects (default is an empty dictionary).
        """
        self.name = name
        self.flights = flights

    def get_all_flights(self):
        """
        Retrieve all flights managed by the airline.

        :return: A dictionary of all flights.
        """ 
        return self.flights

    def get_flight(self, flight_id):
        """
        Retrieve a specific flight by its ID.

        :param flight_id: The ID of the flight to retrieve.
        :return: The flight object associated with the given ID.
        """
        return self.flights[flight_id]

    def get_free_seats(self, flight_id):
        """
        Retrieve the number of free seats for a specific flight.

        :param flight_id: The ID of the flight.
        :return: The number of free seats available.
        """
        return self.flights[flight_id].get_free_seats()
        
    def reserve(self, flight_id, seat_number):
        """
        Temporarily reserve a seat for a specific flight.

        :param flight_id: The ID of the flight.
        :param seat_number: The seat number to reserve.
        """
        flight = self.get_flight(flight_id)
        if flight.is_free(seat_number):
            flight.temporary_reserve_seat(seat_number)

    def confirm_reserve(self, flight_id, seat_number):
        """
        Confirm a temporary reservation for a seat.

        :param flight_id: The ID of the flight.
        :param seat_number: The seat number to confirm.
        """
        flight = self.get_flight(flight_id)
        if flight.is_temporary_reserved(seat_number):
            flight.reserve_seat(seat_number)

    def cancel_reserve(self, flight_id, seat_number):
        """
        Cancel a temporary reservation for a seat.

        :param flight_id: The ID of the flight.
        :param seat_number: The seat number to cancel.
        """
        flight = self.get_flight(flight_id)
        if flight.is_temporary_reserved(seat_number):
            flight.free_seat(seat_number)

    def get_all_seats(self, flight_id):
        """
        Retrieve all seats for a specific flight.

        :param flight_id: The ID of the flight.
        :return: A list of all seats for the flight.
        """
        return self.flight[flight_id].get_seats()        
    
    def __repr__(self):
        """
        Provide a string representation of the airline.

        :return: The name of the airline.
        """
        return self.name
    
    def to_dict(self):
        """
        Convert the airline and its flights into a dictionary representation.

        :return: A dictionary containing the airline's name and its flights.
        """
        return {
            "name": self.name,
            "flights": [flight.to_dict() for flight in self.flights.values()]
        }