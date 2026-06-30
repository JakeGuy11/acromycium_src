from ..ui import UI, UI_Pins
from ..zone import Zone, Interfaceable
import time, logging, threading

# A single instance of the acromycium
class Spore:
    def __init__(self, logger):
        self.logger = logger
        self.ui = None
        self.zones = []
        self.initialized = False
        self.log(f'Started instance of ACROMYCIUM', logging.INFO)

    # Initialize the UI
    def initialize_ui(self):
        current_ui = UI(self.logger)
        current_ui.attach_pin(UI_Pins.E_STOP, 4)
        current_ui.update()

        self.ui = current_ui
        self.log(f'UI initialized', logging.INFO)

    # Auto populate all zones. This will be dealt with with files in the future
    def detect_zones(self):
        self.log(f'Detecting zones', logging.INFO)
        self._add_zone()

    # Add a zone to maintain
    def _add_zone(self):
        z = Zone(self.logger)
        z.attach_interfaceable(Interfaceable.THERMOCOUPLE, 0)
        z.update()
        
        self.zones.append(z)
        self.log(f'Added zone', logging.INFO)

    def run_ui(self):
        self.log('Running UI', logging.INFO)

    def run_zones(self, kill_switch):
        self.log('Running zones', logging.INFO)

    # Log
    def log(self, msg: str, lvl=logging.DEBUG):
        self.logger.log(level=lvl, msg=f'[Master] {msg}')
