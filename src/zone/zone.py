from .io import IO, Interfaceable
from .control import Control

# Object to allow __main__ to control all relevant features
class Zone:
    def __init__(self):
        self.io = IO()
        self.control = Control(self.io)

    # Perform all necessary updates
    def update(self):
        self.control.update()
    
    def get_temp(self):
        return self.control.Temp
    
    def attach_interfaceable(self, out: Interfaceable, pin: int):
        self.io.attach_interfaceable(out, pin)
