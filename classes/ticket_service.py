class TicketService:
    """
    A service to manage tickets and interact with multiple airlines.
    """
  
    def get_flights_by_src(self, flights, src):
        """
        Retrieve flights originating from a specific source.
        :param flights: A list of flights.
        :param src: The source location to filter flights.
        :return: A list of flights starting from the given source.
        """
        return [f for f in flights if f.src == src]
    
    def get_flights(self, flights, src, dest):
        """
        Find all possible paths (sequences of flights) from a source to a destination.

        :param flights: A list of available flights.
        :param src: The starting location.
        :param dest: The target destination.
        :return: A list of flight paths, where each path is a list of flights.
        """
        stack = [(src, [])] # Stack for depth-first search: (current location, path so far)
        paths = []  # List to store all valid paths
        while stack:
            current, path = stack.pop()

            if current == dest: # If destination is reached, add the path to results
                paths.append(path)
                continue
            # Explore flights from the current source
            for flight in self.get_flights_by_src(flights, current):
                # Avoid cycles by checking if the destination is already visited in the path
                if flight.dest not in [f.src for f in path]:
                    stack.append((flight.dest, path + [flight]))
                
        return paths