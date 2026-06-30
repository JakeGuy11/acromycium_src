from enum import Enum
import time, logging

# Define pins for each interfaceable element on the UI
class UI_Pins(Enum):
    E_STOP = 0
    LIGHT_PWR = 1


# Class to interface with hardware for a zone
class IO:
    def __init__(self, logger):
        self.id = round(time.time()*1000)
        self.logger = logger
        self.pins = {
            output: None
            for output in UI_Pins
        }
        self.log(f'Initialized with id {self.id}', logging.INFO)

    # Attach device to pin. placeholder for now
    def attach_pin(self, out: UI_Pins, pin: int):
        self.pins[out] = pin
        self.log(f'Attached device {out} on pin {pin}', logging.INFO)
    
    # Log
    def log(self, msg: str, lvl=logging.DEBUG):
        self.logger.log(level=lvl, msg=f'{self.id}: [UI IO] {msg}')
