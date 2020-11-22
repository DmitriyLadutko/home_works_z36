import logging
import sys

LOG_FILE = 'log_file.txt'


def get_logger():
    logger = logging.getLogger(__name__)

    formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(message)s')
    formatter_stdout = logging.Formatter('%(message)s')

    file_handler = logging.FileHandler(filename=LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    screen_handler = logging.StreamHandler(sys.stdout)
    screen_handler.setLevel(logging.DEBUG)
    screen_handler.setFormatter(formatter_stdout)

    logger.addHandler(file_handler)
    logger.addHandler(screen_handler)

    logger.setLevel(logging.DEBUG)

    return logger
