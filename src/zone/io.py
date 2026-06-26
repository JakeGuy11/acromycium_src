from enum import Enum

# Define pins for each interfaceable element in the zone
class Interfaceable(Enum):
    DRY_HEATER = 0
    DRY_HEATER_FAN = 1

    WET_HEATER = 2
    WET_HEATER_FAN = 3

    CIRC_FAN = 4
    COOLING_FAN = 5

    AMBIENT_TEMP_SCL = 6
    AMBIENT_TEMP_SDA = 7

    THERMOCOUPLE = 8

# Class to interface with hardware for a zone
class IO:
    def __init__(self):
        pass
        self.pins = {
            output: None
            for output in Interfaceable
        }

    def attach_interfaceable(self, out: Interfaceable, pin: int):
        self.pins[out] = pin