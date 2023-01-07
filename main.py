from datetime import datetime

from flask import Flask, request
import HandleRequest, HandleLogging, Independent, Stack
import RequestCounter as rc

app = Flask(__name__)
stack = []
request_logger = HandleRequest.request_logger

@app.route('/independent/calculate', methods=['GET', 'POST'])
def independent_calc():
    if request.method == 'POST':
        rc.increase_req_count()
        start = datetime.now()

        post_body = request.get_json(request.data)
        res = Independent.calc(post_body)

        request_logger.info("Incoming request | #%d | resource: %s | HTTP Verb %s",
                            rc.get_req_count(), request.path, request.method.upper())
        request_logger.debug("request #%d duration: %dms", rc.get_req_count(), datetime.now()-start)
    return res


@app.route('/stack/size', methods=['GET'])
def get_stack_size():
    rc.increase_req_count()
    res = Stack.stack_size(stack)
    return res


@app.route('/stack/arguments', methods=['PUT', 'DELETE'])
def handle_arg():
    rc.increase_req_count()
    if request.method == 'PUT':
        body = request.get_json(request.data)
        res = Stack.add_arguments(stack, body)
        return res
    else:  # delete request
        query_param = dict(request.args)
        res = Stack.delete_arguments(stack, query_param)
        return res


@app.route('/stack/operate', methods=['GET'])
def calc_from_stack():
    rc.increase_req_count()
    query_param = dict(request.args)
    res = Stack.calc(stack, query_param['operation'])
    return res

@app.route('/logs/level', methods=['GET', 'PUT'])
def logs_level():
    rc.increase_req_count()


if __name__ == '__main__':
    app.run(host="localhost", port=8496, debug=True)

