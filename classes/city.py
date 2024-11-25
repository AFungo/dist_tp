from enum import Enum

class City(Enum):

    AEP = 1
    EZE = 2
    RCU = 3

# functional syntax
City = Enum('City', [('AEP', 1), ('EZE', 2), ('RCU', 3)])