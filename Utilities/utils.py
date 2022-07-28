import inspect
import logging


def custom_logger(logLevel=logging.DEBUG):
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    logger.setLevel(logLevel)
    fh = logging.FileHandler("automation.log", mode='w')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
