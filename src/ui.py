from enum import Enum

class UI_Pins(Enum):
    SCREEN_SCL = 0
    SCREEN_SDA = 1

class UI:
    def __init__(self):
        pass
        self.pins = {
            pin: None
            for pin in UI_Pins
        }

    def attach_pin(self, out: Interfaceable, pin: int):
        self.pins[out] = pin