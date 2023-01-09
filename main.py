from datetime import datetime

from flask import Flask, request
import Independent, Stack
import LogLevel
import RequestCounter as rc
import HandleRequest as hr

app = Flask(__name__)
stack = []
request_logger = hr.request_logger

@app.route('/',methods =['GET'])
def nothing():
    return "Hey Idob"

@app.route('/independent/calculate', methods=['GET', 'POST'])
def independent_calc():
    if request.method == 'POST':
        start = datetime.now()
        rc.increase_req_count()

        post_body = request.get_json(request.data)
        res = Independent.calc(post_body)

        hr.request_log(request.path, request.method.upper(), start)
    return res


@app.route('/stack/size', methods=['GET'])
def get_stack_size():
    start = datetime.now()
    rc.increase_req_count()

    res = Stack.stack_size(stack)

    hr.request_log(request.path, request.method.upper(), start)
    return res


@app.route('/stack/arguments', methods=['PUT', 'DELETE'])
def handle_arg():
    start = datetime.now()
    rc.increase_req_count()

    if request.method == 'PUT':
        body = request.get_json(request.data)
        res = Stack.add_arguments(stack, body)
    else:  # delete request
        query_param = dict(request.args)
        res = Stack.delete_arguments(stack, query_param)

    hr.request_log(request.path, request.method.upper(), start)
    return res


@app.route('/stack/operate', methods=['GET'])
def calc_from_stack():
    start = datetime.now()
    rc.increase_req_count()
    query_param = dict(request.args)

    res = Stack.calc(stack, query_param['operation'])

    hr.request_log(request.path, request.method.upper(), start)
    return res

@app.route('/logs/level', methods=['GET', 'PUT'])
def logs_level():
    start = datetime.now()
    rc.increase_req_count()
    logger_name = dict(request.args)['logger-name']

    if request.method == 'GET':
        res = LogLevel.get_log_level(logger_name)

    else: # method 'PUT'
        logger_level = dict(request.args)['logger-level']
        res = LogLevel.set_log_level(logger_name, logger_level)
    hr.request_log(request.path, request.method.upper(), start)
    return res

if __name__ == '__main__':
    app.run(host="localhost", port=9583, debug=True)

