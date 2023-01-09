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


# This function handle requests log
def request_log(path, method, start):
    request_logger.info("Incoming request | #%d | resource: %s | HTTP Verb %s",
                        rc.get_req_count(), path, method)
    request_logger.debug(f"request #{rc.get_req_count()} duration: {int(duration(start))}ms")


# This function calculate the time diff from start operation to finish
def duration(start):
    start_time = datetime.strptime(start, date_format)
    end_time = datetime.strptime(get_time(), date_format)
    diff = end_time - start_time
    ms = diff.total_seconds() * 1000
    return ms


# This function calculate the time according to specific date format
def get_time():
    time = datetime.now().strftime(date_format)[:-3]
    return time
