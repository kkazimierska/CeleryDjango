import logging

from typing_extensions import Protocol


class Logger(Protocol):

    def info(self, message: str):
        pass

    def warn(self, message: str):
        pass

    def error(self, message: str):
        pass


class DefaultTaskLogger(Logger):
    """
    This task logger will only push messages to default logging system, so the information isn't lost.
    It can be used as context manager to automatically print begin and finish messages
    """

    task_name = None

    def __enter__(self):
        self.info(f'Begun {self.task_name}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if any([exc_type, exc_val, exc_tb]):
            self.error(f'Failed {self.task_name}', finished=True)
        else:
            self.info(f'Finished {self.task_name}', finished=True)

    def info(self, message: str, *args, **kwargs):
        logging.info(message)

    def error(self, message: str, *args, **kwargs):
        logging.error(message)

    def warn(self, message: str, *args, **kwargs):
        logging.warning(message)