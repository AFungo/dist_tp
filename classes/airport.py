from enum import Enum

class Airport(Enum):
    AEP = 1
    EZE = 2
    RCU = 3
    GDZ = 4

# functional syntax
Airport = Enum('Airport', [('AEP', 1), ('EZE', 2), ('RCU', 3), ('GDZ', 4)])