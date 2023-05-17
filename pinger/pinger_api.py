from messaging.task_logger import DefaultTaskLogger, Logger

class Pinger:
    def __init__(
        self, windfarm_name = None,
        logger: Logger = None,
    ):
        self.logger = logger if logger else DefaultTaskLogger()
        self.windfarm_name = windfarm_name

    def run_pinger_api(self):
        print('Can execute pinger api.')