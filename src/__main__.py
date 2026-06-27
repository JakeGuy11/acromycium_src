from .ui import *
from .zone import Zone, Interfaceable
import logging, datetime

logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(asctime)s  %(levelname)s] %(message)s', datefmt='%Y/%m/%d %H:%M:%S', filename=f'logs/{datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.log', encoding='utf-8', level=logging.DEBUG)

if __name__ == '__main__':
    current_ui = UI(logger)
    current_ui.attach_pin(UI_Pins.E_STOP, 4)
    print("UI initialized successfully")

    zone_1 = Zone(logger)
    zone_1.attach_interfaceable(Interfaceable.THERMOCOUPLE, 0)
    print("Zones initialized successfully")

    zone_1.update()
    print(zone_1.get_temp())
    print("Zone updated successfully")