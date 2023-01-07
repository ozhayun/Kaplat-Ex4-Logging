import HandleRequest as hr
import Calculator
from flask import Response

independent_logger = hr.independent_logger


# This function calculate from number/s and operation
def calc(request, post_body):
    op = post_body['operation'].lower()
    args = post_body['arguments']
    num_of_args = len(args)
    is_valid_and_kind = Calculator.is_valid_op(op)

    # No such operation Error 409
    if is_valid_and_kind == 0:
        return not_such_op(post_body)

    # Not enough arguments Error 409
    if num_of_args == 0 or (num_of_args == 1 and is_valid_and_kind == 2):
        return not_enough_args(post_body)

    # Unary operation
    if num_of_args == 1 and is_valid_and_kind == 1:
        return independent_unary_op(op, args)

    # Binary operation
    if num_of_args == 2 and is_valid_and_kind == 2:
        return independent_binary_op(op, args)

    # Too many arguments Error 409
    else:
        return too_many_args(post_body)


def independent_unary_op(op, args):
    if op == 'fact' and args[0] < 0:
        independent_logger.error("Server encountered an error ! message:"
                                 " Error while performing operation Factorial: not supported for "
                                                 "the negative number")

        return Response(hr.convert_to_json(None, "Error while performing operation Factorial: not supported for "
                                                 "the negative number"), status=409)
    val = Calculator.calc_unary_op(op, args[0])

    independent_logger.info("Performing operation %s. Result is %s", op, val)
    independent_logger.debug("Performng operation: %s(%s) = %s", op, args[0], val)

    return Response(hr.convert_to_json(val, None), 200)


def independent_binary_op(op, args):
    if op == 'divide' and args[1] == 0:  # Divide by zero is illegal
        independent_logger.error("Server encountered an error ! message:"
                                 " Error while performing operation Divide: division by 0")
        return Response(hr.convert_to_json(None, "Error while performing operation Divide: division by 0"),
                        status=409)
    val = Calculator.calc_binary_op(op, args[0], args[1])

    independent_logger.info("Performing operation %s. Result is %s", op, val)
    independent_logger.debug("Performng operation: %s(%s,%s) = %s", op, args[0], args[1], val)

    return Response(hr.convert_to_json(val, None), 200)


def not_such_op(post_body):
    independent_logger.error("Server encountered an error ! message: Error: unknown operation: " +
                             str(post_body['operation']))
    return Response(hr.convert_to_json(None, "Error: unknown operation: " +
                                       str(post_body['operation'])), status=409)


def not_enough_args(post_body):
    independent_logger.error("Server encountered an error ! message:"
                             " Error: Not enough arguments to perform the operation " +
                             str(post_body['operation']))
    return Response(hr.convert_to_json(None, "Error: Not enough arguments to perform the operation " +
                                       str(post_body['operation'])), status=409)


def too_many_args(post_body):
    independent_logger.error("Server encountered an error ! message:"
                             " Error: Too many arguments to perform the operation " +
                             str(post_body['operation']))
    return Response(hr.convert_to_json(None, "Error: Too many arguments to perform the operation " +
                                       str(post_body['operation'])), status=409)
