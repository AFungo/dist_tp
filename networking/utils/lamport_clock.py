class LamportClock:
    def __init__(self):
        self.time = 0

    def increment(self):
        self.time += 1

    def update(self, received_time):
        self.time = max(self.time + 1, received_time)

    def get_time(self):
        return self.time
