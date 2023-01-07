from flask import json
import HandleLogging as hl

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
