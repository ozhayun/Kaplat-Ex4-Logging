from flask import Flask, request
import handle_req, handle_logging

app = Flask(__name__)
req_count = 1
stack = []

@app.route('/independent/calculate', methods=['GET', 'POST'])
def independent_calc():
    if request.method == 'POST':

        handle_logging.try_log()

        post_body = request.get_json(request.data)
        # print(post_body)
        result = handle_req.independent_calc(post_body)
        # print(result.get_data())
    return result


@app.route('/stack/size', methods=['GET'])
def get_stack_size():
    return handle_req.stack_size(len(stack))


@app.route('/stack/arguments', methods=['PUT', 'DELETE'])
def handle_arg():

    if request.method == 'PUT':
        body = request.get_json(request.data)
        res = handle_req.add_arguments(stack, body)
        # print("add args")
        # print(stack)
        return res
    else:  # delete request
        # print("Before delete")
        # print(stack)
        query_param = dict(request.args)
        res = handle_req.delete_arguments(stack, query_param)
        # print("delete args")
        # print("stack Size: " + str(res.get_data()))
        # print(stack)
        return res


@app.route('/stack/operate', methods=['GET'])
def calc_from_stack():
    # print("Calc from stack, current size: " + str(len(stack)))
    query_param = dict(request.args)
    res = handle_req.calc_from_stack(stack, query_param['operation'])
    # print(res.get_data())
    # print("Current size: " + str(len(stack)))
    return res


if __name__ == '__main__':
    app.run(host="localhost", port=8496, debug=True)
