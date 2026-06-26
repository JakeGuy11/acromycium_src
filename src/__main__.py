from .ui import *
from .zone import Zone, Interfaceable

if __name__ == '__main__':
    current_ui = UI()
    current_ui.attach_pin(UI_Pins.SCREEN_SCL, 4)
    current_ui.attach_pin(UI_Pins.SCREEN_SDA, 5)
    print("UI initialized successfully")

    zone_1 = Zone()
    zone_1.attach_interfaceable(Interfaceable.THERMOCOUPLE, 0)
    print("Zones initialized successfully")

    zone_1.update()
    print(zone_1.get_temp())
    print("Zone updated successfully")