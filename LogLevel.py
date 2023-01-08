import json

import HandleRequest as hr
from flask import Response

levels = {
    0: 'NOTSET',
    10: 'DEBUG',
    20: 'INFO',
    30: 'WARN',
    40: 'ERROR',
    50: 'CRITICAL'}

request_logger = hr.request_logger
stack_logger = hr.stack_logger
independent_logger = hr.independent_logger


def get_log_level(logger_name):
    if logger_name == 'request_logger':
        return Response(json.dumps(levels[request_logger.getEffectiveLevel()]), status=200)
    if logger_name == 'stack_logger':
        return Response(json.dumps(levels[stack_logger.getEffectiveLevel()]), status=200)
    if logger_name == 'independent_logger':
        return Response(json.dumps(levels[independent_logger.getEffectiveLevel()]), status=200)
    return Response(json.dumps("Logger not exists"), status=409)

