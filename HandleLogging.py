import logging
import os
import sys

format = "%(asctime)s.%(msecs)03d %(levelname)s: %(message)s"
datefmt = "%d-%m-%Y %H:%M:%S"


def create_logs_directory():
    # Create logs directory
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


def req_log(msg, level, duration):
    global req_count
    if level == logging.INFO:
        request_logger.info(msg + " | request #%d | resource: %s |"
                                  " HTTP Verb %s", req_count)
    else:
        request_logger.debug("request #%d duration: %sms", req_count, duration)
    req_count += 1


def stack_log(msg, level):
    global req_count
    if level == logging.INFO:
        stack_logger.debug(msg + " | request #%d", req_count)
    req_count += 1


def ind_log(msg, level):
    global req_count
    independent_logger.info(msg + " | request #%d", req_count)
    req_count += 1


# def log(logger, level, msg):
#     if level == logging.INFO:
#         logger.info(msg, main.req_count)
#     else:
#         logger.debug(msg, main.req_count)
#     main.req_count = main.req_count + 1


# def increase_request_count():
#     req_count += 1


def log_setup(log_name, file_name, log_level=logging.INFO, stream=sys.stdout):
    logger = logging.getLogger(log_name)
    formatter = logging.Formatter(format)

    fileHandler = logging.FileHandler(filename=r"logs/" + file_name, mode='w')
    fileHandler.setFormatter(formatter)

    logger.setLevel(log_level)
    logger.addHandler(fileHandler)

    if log_name == 'request-logger':
        streamHandler = logging.StreamHandler(stream=stream)
        logger.addHandler(streamHandler)

    return logger

    # logger = logging.getLogger(log_name)
    # return logging.basicConfig(
    #     level=log_level,
    #     format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
    #     datefmt='%d-%m-%Y %H:%M:%S',
    #     handlers=[
    #         logging.FileHandler(filename=r"logs/" + file_name, mode='w'),
    #         logging.StreamHandler(stream=sys.stdout)
    #     ])


# def try_log():
# log_format = "%(asctime)s.%(msecs)03d %(levelname)s: %(message)s"
# logger = logging.getLogger("req_log")
# logger.setLevel("INFO")
# file_handler = logging.FileHandler(filename=r"logs/requests.log", mode='w')
# file_handler.setFormatter(logging.Formatter(log_format))
# logger.addHandler(file_handler)
# logger.addHandler(logging.StreamHandler(stream=sys.stdout))
# logger.info("Info message | request #%d", main.req_count)

# logging.basicConfig(
#     level=logging.INFO,
#     # filename=r"logs/requests.log",
#     #filemode='w',
#     format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
#     datefmt='%d-%m-%Y %H:%M:%S',
#     handlers=[
#         logging.FileHandler(filename=r"logs/requests.log", mode='w'),
#         logging.StreamHandler(stream=sys.stdout)
#     ])
# logging.info("Info message | request #%d", main.req_count)
# main.req_count = main.req_count + 1

request_logger = init_request_logger()
stack_logger = init_stack_logger()
independent_logger = init_independent_logger()
