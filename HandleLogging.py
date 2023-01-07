import logging
import os
import sys

format = "%(asctime)s.%(msecs)03d %(levelname)s: %(message)s"
datefmt = "%d-%m-%Y %H:%M:%S"

if not os.path.exists(os.getcwd() + "/logs"):
    os.makedirs(os.getcwd() + "/logs")


def init_request_logger():
    logger = logging.getLogger("request-logger")
    formatter = logging.Formatter(format, datefmt)

    fileHandler = logging.FileHandler(filename=r"logs/requests.log", mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler(stream=sys.stdout)

    logger.setLevel(logging.INFO)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)

    return logger


def init_stack_logger():
    logger = logging.getLogger("stack-logger")
    formatter = logging.Formatter(format, datefmt)

    fileHandler = logging.FileHandler(filename=r"logs/stack.log", mode='w')
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.addHandler(fileHandler)

    return logger


def init_independent_logger():
    logger = logging.getLogger("independent-logger")
    formatter = logging.Formatter(format, datefmt)

    fileHandler = logging.FileHandler(filename=r"logs/independent.log", mode='w')
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)

    return logger
