class NodeLog:
    def __init__(self):
        self.log = []  # operations

    def add_entry(self, transaction_id, flights_id, seats_amount, status):
        """
        Add an entry to the log.
        """
        self.log.append({
            "transaction_id": transaction_id,
            "flights_id": flights_id,
            "seats_amount": seats_amount,
            "status": status  # "pending", "committed", "aborted"
        })

    def get_conflicting_entries(self, flights_id):
        """
        Check for conflicting entries in the log.
        """
        return [entry for entry in self.log if flights_id in entry["flights_id"] and entry["status"] == "committed"]
