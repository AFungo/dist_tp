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

    def reserve(self, flight_id, seats_amount):
        """
        Temporarily reserve a seat for a specific flight.

        :param flight_id: The ID of the flight.
        :param seats_amount: The amount of seats to reserve.
        """
        flight = self.get_flight(flight_id)
        if flight.are_seats_available(seats_amount):
            flight.temporary_reserve_seat(seats_amount)

    def confirm_reserve(self, flight_id, seats_amount):
        """
        Confirm a temporary reservation for a seat.

        :param flight_id: The ID of the flight.
        :param seats_amount: The amount of seats to confirm.
        """
        flight = self.get_flight(flight_id)
        if flight.is_temporary_reserved(seats_amount):
            flight.reserve_seat(seats_amount)

    def cancel_reserve(self, flight_id, seats_amount):
        """
        Cancel a temporary reservation for a seat.

        :param flight_id: The ID of the flight.
        :param seats_amount: The amount of seats to cancel.
        """
        flight = self.get_flight(flight_id)
        if flight.is_temporary_reserved(seats_amount):
            flight.free_seat(seats_amount)

    def get_seats_available(self, flight_id):
        """
        Retrieve all seats for a specific flight.

        :param flight_id: The ID of the flight.
        :return: A list of all seats for the flight.
        """
        return self.flight[flight_id].get_seats_available()        
    
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