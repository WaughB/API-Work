# logger.py
import logging
import os
from datetime import datetime


class log_this:
    def __init__(self, name, log_file=None, level=logging.INFO):
        """
        Initialize the logger.

        :param name: Name for the logger, usually __name__ of the module where it's used.
        :param log_file: Path to the log file. If None, logs are printed to console.
        :param level: Logging level, e.g., logging.INFO, logging.DEBUG.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File handler to log messages in a file
        if log_file is None:
            os.makedirs("./logs", exist_ok=True)
            log_file = f"logs/{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # Console handler to log messages to the console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
