from datetime import datetime

from flask import Flask, request
import Independent, Stack
import RequestCounter as rc
import HandleRequest as hr

app = Flask(__name__)
stack = []
request_logger = hr.request_logger

@app.route('/independent/calculate', methods=['GET', 'POST'])
def independent_calc():
    if request.method == 'POST':
        start = datetime.now()
        rc.increase_req_count()

        post_body = request.get_json(request.data)
        res = Independent.calc(post_body)

        # request_logger.info("Incoming request | #%d | resource: %s | HTTP Verb %s",
        #                     rc.get_req_count(), request.path, request.method.upper())
        # request_logger.debug("request #%d duration: %dms", rc.get_req_count(), datetime.now()-start)
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

    hr.request_log(request.path, request.method.upper(), start)


if __name__ == '__main__':
    app.run(host="localhost", port=9583, debug=True)

