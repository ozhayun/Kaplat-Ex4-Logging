from flask import Flask, request
import HandleRequest, HandleLogging, RequestCounter, Independent, Stack

app = Flask(__name__)
stack = []


@app.route('/independent/calculate', methods=['GET', 'POST'])
def independent_calc():
    if request.method == 'POST':
        post_body = request.get_json(request.data)
        result = Independent.calc(request, post_body)
    return result


@app.route('/stack/size', methods=['GET'])
def get_stack_size():
    return Stack.stack_size(stack)


@app.route('/stack/arguments', methods=['PUT', 'DELETE'])
def handle_arg():

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
    query_param = dict(request.args)
    res = Stack.calc(stack, query_param['operation'])
    return res


if __name__ == '__main__':
    app.run(host="localhost", port=8496, debug=True)

