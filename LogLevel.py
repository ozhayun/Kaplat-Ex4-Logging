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
    if logger_name == 'request-logger':
        return Response(json.dumps(levels[request_logger.getEffectiveLevel()]), status=200)
    if logger_name == 'stack-logger':
        return Response(json.dumps(levels[stack_logger.getEffectiveLevel()]), status=200)
    if logger_name == 'independent-logger':
        return Response(json.dumps(levels[independent_logger.getEffectiveLevel()]), status=200)
    return Response("Logger: %s, not exists", logger_name, status=409)


def set_log_level(logger_name, logger_level):
    logger_level = logger_level.upper()
    if logger_level in levels.values():
        if logger_name == 'request-logger':
            request_logger.setLevel(logger_level)                               #### check if  log lower case
            return Response(json.dumps(logger_level.upper()), status=200)

        if logger_name == 'stack-logger':
            stack_logger.setLevel(logger_level)
            return Response(json.dumps(logger_level.upper()), status=200)

        if logger_name == 'independent-logger':
            independent_logger.setLevel(logger_level)
            return Response(json.dumps(logger_level.upper()), status=200)
        return Response(json.dumps("Logger not exists"), status=409)
    return Response(json.dumps("Log level not exists"), status=409)


