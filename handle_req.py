import calculator as calc
from flask import Response, json

# This function calculate from number/s and operation
def independent_calc(post_body):
    op = post_body['operation'].lower()
    args = post_body['arguments']
    num_of_args = len(args)
    is_valid_and_kind = calc.is_valid_op(op)

    # No such operation Error 409
    if is_valid_and_kind == 0:
        return Response(convert_to_json(None, "Error: unknown operation: " +
                                        str(post_body['operation'])), status=409)

    # Not enough arguments Error 409
    if num_of_args == 0 or (num_of_args == 1 and is_valid_and_kind == 2):
        return Response(convert_to_json(None, "Error: Not enough arguments to perform the operation " +
                                        str(post_body['operation'])), status=409)

    # Unary operation
    if num_of_args == 1 and is_valid_and_kind == 1:
        if op == 'fact' and args[0] < 0:
            return Response(convert_to_json(None, "Error while performing operation Factorial: not supported for "
                                                  "the negative number"), status=409)
        val = calc.calc_unary_op(op, args[0])
        return Response(convert_to_json(val, None), 200)

    # Binary operation
    if num_of_args == 2 and is_valid_and_kind == 2:
        if op == 'divide' and args[1] == 0:  # Divide by zero is illegal
            return Response(convert_to_json(None, "Error while performing operation Divide: division by 0"),
                            status=409)
        val = calc.calc_binary_op(op, args[0], args[1])
        return Response(convert_to_json(val, None), 200)

    # Too many arguments Error 409
    else:
        # if num_of_args == 2 and is_valid_and_kind == 1:
        return Response(convert_to_json(None, "Error: Too many arguments to perform the operation " +
                                        str(post_body['operation'])), status=409)


def stack_size(size):
    return Response(convert_to_json(size, None), 200)


def add_arguments(stack, put_body):
    args = put_body['arguments']

    for i in args:
        if not isinstance(i, int):
            return Response(convert_to_json(None, "Error: not all arguments are valid"), 409)

    for i in args:
        stack.append(i)
    return Response(convert_to_json(len(stack), None), 200)


def calc_from_stack(stack, operation):
    is_valid_op = calc.is_valid_op(operation)

    # Binary operation
    if is_valid_op == 2:
        if len(stack) >= 2:
            x = stack.pop()
            y = stack.pop()
            if operation == 'divide' and y == 0:  # Divide by zero is illegal
                return Response(convert_to_json(None, "Error while performing operation Divide: division by 0"),
                                status=409)
            return Response(convert_to_json(calc.calc_binary_op(operation, x, y), None), status=200)
        # Not enough arguments
        else:
            return Response(convert_to_json(None, "Error: cannot implement operation " + str(operation) +
                                            ". It requires " + str(is_valid_op) + " arguments and the stack has only " +
                                            str(len(stack)) + " arguments"), status=409)
    # Unary operation
    if is_valid_op == 1:
        if len(stack) >= 1:
            x = stack.pop()
            if x < 0 and operation == 'fact':
                return Response(convert_to_json(None, "Error while performing operation Factorial: not supported for "
                                                      "the negative number"), status=409)
            return Response(convert_to_json(calc.calc_unary_op(operation, x), None), status=200)
        # Not enough arguments
        else:
            return Response(convert_to_json(None, "Error: cannot implement operation " + str(operation) +
                                            ". It requires " + str(is_valid_op) + " arguments and the stack has only " +
                                            str(len(stack)) + " arguments"), status=409)
    # No such operation
    else:
        return Response(convert_to_json(None, "Error: unknown operation: " + str(operation)), status=409)


# This function is for deleting some arguments from stack
def delete_arguments(stack, delete_body):
    args = int(delete_body['count'])
    if args <= len(stack):
        for i in range(args):
            stack.pop()
        return Response(convert_to_json(len(stack), None), 200)
    return Response(convert_to_json(None, "Error: cannot remove " + str(args) + " from the stack. It has only " +
                                    str(len(stack)) + " arguments"), status=409)


# This function is for format result or error message into json as a response of the server
def convert_to_json(result, error_message):
    if result is None:
        response = json.dumps({'error-message': error_message})
        # json = jsonify('error-message', error_message)
    else:
        response = json.dumps({'result': result})
        # json = jsonify('result', result)
    return response
