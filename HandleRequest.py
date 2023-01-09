from datetime import datetime

from flask import json
import HandleLogging as hl
import RequestCounter as rc

request_logger = hl.init_request_logger()
stack_logger = hl.init_stack_logger()
independent_logger = hl.init_independent_logger()
date_format = "%d-%m-%Y %H:%M:%S.%f"


# This function is for format result or error message into json as a response of the server
def convert_to_json(result, error_message):
    if result is None:
        response = json.dumps({'error-message': error_message})
    else:
        response = json.dumps({'result': result})
    return response


def request_log(path, method, start):
    request_logger.info("Incoming request | #%d | resource: %s | HTTP Verb %s",
                        rc.get_req_count(), path, method)
    request_logger.debug(f"request  # {rc.get_req_count()} duration: {int(duration(start))}ms")


def duration(start):
    start_time = datetime.strptime(str(start), date_format)
    end_time = datetime.strptime(get_time(), date_format)
    diff = end_time - start_time
    ms = diff.total_seconds() * 1000

    # end = get_time()
    # diff = end - start
    # diff = diff.total_seconds()
    # diff = diff * 1000
    return ms


def get_time():
    time = datetime.now().strftime(date_format)[:-3]
    return time






    # time_format = '%d-%m-%Y %H:%M:%S.%f'
    # start = datetime.strptime(start_time, time_format)
    # end = datetime.strptime(get_time(), time_format)
    # time = end - start
    # ms = time.total_seconds() * 1000
    # date = get_time()
    # log_message = f"request #{counter} duration: {int(ms)}ms"
    # request_logger.debug(f'{date} {"DEBUG"}: {log_message} |'f' request #{counter}')






    # end = datetime.now()
    # diff = end - start
    # diff = diff.total_seconds()
    # diff = diff * 1000

    # return diff












# def request_log(path, method, start):
#     # diff = (datetime.now() - start).total_seconds() * 1000
#     diff = duration(start)
#     request_logger.info("Incoming request | #%d | resource: %s | HTTP Verb %s",
#                         rc.get_req_count(), path, method)
#     # request_logger.debug(f"request  # {rc.get_req_count()} duration: {diff}ms")
#     request_logger.debug("request  # %d duration: %fms", rc.get_req_count(), diff)
#     request_logger.debug(f"request  # {rc.get_req_count()} duration: {duration(start)}ms")
#
#
# def duration(start):
#     print("Start: ", start)
#     end = datetime.now()
#     print("End: ", end)
#     diff = end - start
#     print("end - start: ", diff)
#     diff = diff.total_seconds()
#     print("(start - end).total_seconds()): ", diff)
#     diff = diff * 1000
#     print("(start - end).total_seconds()) * 1000: ", diff)
#
#     return diff
