import logging
import os
import sys
import ArgFilterFile


format = "%(asctime)s.%(msecs)03d %(levelname)s: %(message)s | request #%(arg)s"
date_format = "%d-%m-%Y %H:%M:%S"


# create logs folder in project directory
if not os.path.exists(os.getcwd() + "/logs"):
    os.makedirs(os.getcwd() + "/logs")


# This function init request-loggr
def init_request_logger():
    logger = logging.getLogger("request-logger")
    formatter = logging.Formatter(format, date_format)

    fileHandler = logging.FileHandler(filename=r"logs/requests.log", mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler(stream=sys.stdout)

    logger.setLevel(logging.INFO)
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    logger.addFilter(ArgFilterFile.ArgFilter())

    return logger


# This function init stack-loggr
def init_stack_logger():
    logger = logging.getLogger("stack-logger")
    formatter = logging.Formatter(format, date_format)

    fileHandler = logging.FileHandler(filename=r"logs/stack.log", mode='w')
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.INFO)
    logger.addHandler(fileHandler)
    logger.addFilter(ArgFilterFile.ArgFilter())

    return logger


# This function init independent-loggr
def init_independent_logger():
    logger = logging.getLogger("independent-logger")
    formatter = logging.Formatter(format, date_format)

    fileHandler = logging.FileHandler(filename=r"logs/independent.log", mode='w')
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    logger.addFilter(ArgFilterFile.ArgFilter())

    return logger
