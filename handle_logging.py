import logging
import os
import sys
import main


def try_log():
    # log_format = "%(asctime)s.%(msecs)03d %(levelname)s: %(message)s"
    # logger = logging.getLogger("req_log")
    # logger.setLevel("INFO")
    # file_handler = logging.FileHandler(filename=r"logs/requests.log", mode='w')
    # file_handler.setFormatter(logging.Formatter(log_format))
    # logger.addHandler(file_handler)
    # logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    # logger.info("Info message | request #%d", main.req_count)

    # Create logs directory
    if not os.path.exists(os.getcwd() + "/logs"):
        os.makedirs(os.getcwd() + "/logs")

    logging.basicConfig(
        level=logging.INFO,
        # filename=r"logs/requests.log",
        #filemode='w',
        format="%(asctime)s.%(msecs)03d %(levelname)s: %(message)s",
        datefmt='%d-%m-%Y %H:%M:%S',
        handlers=[
            logging.FileHandler(filename=r"logs/requests.log", mode='w'),
            logging.StreamHandler(stream=sys.stdout)
        ])
    logging.info("Info message | request #%d", main.req_count)
    main.req_count = main.req_count + 1


