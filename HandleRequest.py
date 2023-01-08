from datetime import datetime

from flask import json
import HandleLogging as hl
import RequestCounter as rc

request_logger = hl.init_request_logger()
stack_logger = hl.init_stack_logger()
independent_logger = hl.init_independent_logger()


# This function is for format result or error message into json as a response of the server
def convert_to_json(result, error_message):
    if result is None:
        response = json.dumps({'error-message': error_message})
    else:
        response = json.dumps({'result': result})
    return response



def request_log(path, method, start):
    diff = (datetime.now() - start).total_seconds() * 1000
    request_logger.info("Incoming request | #%d | resource: %s | HTTP Verb %s",
                        rc.get_req_count(), path, method)
    request_logger.debug(f"request #{rc.get_req_count()} duration: {diff}ms")