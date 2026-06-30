from .ui import *
from .zone import Zone, Interfaceable
from .spore import Spore
import logging, datetime, threading, sys

logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(asctime)s  %(levelname)s] %(message)s', datefmt='%Y/%m/%d %H:%M:%S', filename=f'logs/{datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.log', encoding='utf-8', level=logging.DEBUG)

def main():
    spore = Spore(logger)
    spore.initialize_ui()
    spore.detect_zones()

    start_loop(spore)

def start_loop(spore):
    # Set up the control thread
    kill_all = threading.Event()
    control_thread = threading.Thread(
        target=spore.run_zones,
        args=[kill_all],
        daemon=True
    )

    # Start monitoring the zones
    control_thread.start()

    # Run the UI, ensure safe failure
    try:
        spore.run_ui()
    finally:
        kill_all.set()
        control_thread.join()
        sys.exit(0)

if __name__ == '__main__':
    logger.log(msg=f'[Master] ACROMYCIUM Initiation', level=logging.INFO)
    main()
