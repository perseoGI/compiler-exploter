import logging
import tempfile
import os


def create_file_logger(filename: str) -> tuple[logging.Logger, str]:
    log_file_path = os.path.join(tempfile.gettempdir(), filename)
    # Create a logger instance
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create a file handler and set its level to INFO
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)

    # Create a formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)
    return logger, log_file_path
