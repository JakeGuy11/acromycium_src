from enum import Enum
import time, logging

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
    def __init__(self, logger):
        self.id = round(time.time()*1000)
        self.logger = logger
        self.pins = {
            output: None
            for output in Interfaceable
        }
        self.log(f'Zone[IO] initialized with id {self.id}', logging.INFO)

    # Attach a device
    def attach_interfaceable(self, out: Interfaceable, pin: int):
        self.pins[out] = pin
        self.log(f'Attached device {out} on pin {pin}', logging.DEBUG)
    
    # Log
    def log(self, msg: str, lvl=logging.DEBUG):
        self.logger.log(level=lvl, msg=f'{self.id}: [Zone IO] {msg}')
