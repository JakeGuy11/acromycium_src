import logging, time

class Control:
    def __init__(self, io, logger):
        self.id = round(time.time()*1000)
        self.logger = logger
        self.io = io
        self.log(f'Initialized with id {self.id}', logging.INFO)

    # Perform update
    def update(self):
        self.log('Beginning update cycle', logging.DEBUG)

    # Log
    def log(self, msg: str, lvl=logging.DEBUG):
        self.logger.log(level=lvl, msg=f'{self.id}: [UI Control] {msg}')
