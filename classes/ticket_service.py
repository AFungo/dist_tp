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
        stack = [(src, [])]
        paths = []
        while stack:
            current, path = stack.pop()

            if current == dest:
                paths.append(path)
                continue

            for flight in self.get_flights_by_src(flights, current):
                if flight.dest not in [f.src for f in path]:
                    stack.append((flight.dest, path + [flight]))
                
        return paths
