from enum import Enum
import time, datetime, logging

# Define pins for each interfaceable element on the UI
class UI_Pins(Enum):
    E_STOP = 0

# Class to interface with hardware for a zone
class IO:
    def __init__(self, logger):
        self.id = round(time.time()*1000)
        self.logger = logger
        self.pins = {
            output: None
            for output in UI_Pins
        }
        self.log(f'System UI[IO Interface] initialized with id {self.id}', logging.INFO)

    def attach_pin(self, out: UI_Pins, pin: int):
        self.pins[out] = pin
    
    def log(self, msg: str, lvl=logging.DEBUG):
        self.logger.log(level=lvl, msg=f'{self.id}: {msg}')
