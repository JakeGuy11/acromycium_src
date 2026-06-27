from .io import IO, UI_Pins
from .control import Control
import time, logging

# Object to allow __main__ to control all relevant features
class UI:
    def __init__(self, logger):
        self.id = round(time.time()*1000)
        self.logger = logger
        self.io = IO(logger)
        self.control = Control(self.io, logger)
        self.log(f'System UI initialized with id {self.id}', logging.INFO)

    # Perform all necessary updates
    def update(self):
        self.control.update()
    
    def attach_pin(self, out: UI_Pins, pin: int):
        self.io.attach_pin(out, pin)

    def log(self, msg: str, lvl=logging.DEBUG):
        self.logger.log(level=lvl, msg=f'{self.id}: {msg}')
