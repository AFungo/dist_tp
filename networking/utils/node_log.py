from enum import Enum

class LogStatus(Enum):
    PENDING = "PENDING"
    COMMITTED = "COMMITTED"
    ABORTED = "ABORTED"
    
class NodeLog:
    def __init__(self, flights_id, seats_amount, timestamp):
        self.flights_id = flights_id
        self.seats_amount = seats_amount
        self.status = LogStatus.PENDING
        self.timestamp = timestamp
        
    def is_pending(self):
        return self.status == LogStatus.PENDING
                
    def set_status_pending(self):
        self.status = LogStatus.PENDING
        
    def set_status_committed(self):
        self.status = LogStatus.COMMITTED
        
    def set_status_aborted(self):
        self.status = LogStatus.ABORTED
        