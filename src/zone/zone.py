from .io import IO, Interfaceable
from .control import Control
import logging, time

# Object to allow __main__ to control all relevant features
class Zone:
    def __init__(self, logger):
        self.id = round(time.time()*1000)
        self.logger = logger
        self.io = IO(logger)
        self.control = Control(self.io, logger)
        self.log(f'Initialized with id {self.id}', logging.INFO)

    # Perform all necessary updates
    def update(self):
        self.control.update()
        self.log(f'Beginning update cycle', logging.DEBUG)
    
    # Attach a device
    def attach_interfaceable(self, out: Interfaceable, pin: int):
        self.io.attach_interfaceable(out, pin)
        self.log(f'Attached device {out} on pin {pin}', logging.DEBUG)

    # Log
    def log(self, msg: str, lvl=logging.DEBUG):
        self.logger.log(level=lvl, msg=f'{self.id}: [Zone Master] {msg}')