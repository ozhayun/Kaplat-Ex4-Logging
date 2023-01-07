import logging

import Calculator
from flask import Response
import HandleRequest as hr

stack_logger = hr.stack_logger


def stack_size(stack):
    stack_logger.setLevel(logging.DEBUG)
    stack_logger.info("Stack size is %d", len(stack))
    stack_logger.debug("Stack content (first == top): [" + ','.join(str(v) for v in reversed(stack)) + "]")
    stack_logger.setLevel(logging.INFO)
    return Response(hr.convert_to_json(len(stack), None), 200)


def add_arguments(stack, put_body):
    args = put_body['arguments']
    stack_size_before = len(stack)

    for i in args:
        if not isinstance(i, int):
            return Response(hr.convert_to_json(None, "Error: not all arguments are valid"), 409)

    for i in args:
        stack.append(i)

    stack_logger.setLevel(logging.DEBUG)
    stack_logger.info("Adding total of %d argument(s) to the stack | Stack size: %d", len(args), len(stack))
    stack_logger.debug("Adding arguments: " + ','.join(str(a) for a in args) + " |"
                       " Stack size before %d |"
                       " stack size after %d", stack_size_before, len(stack))
    stack_logger.setLevel(logging.INFO)

    return Response(hr.convert_to_json(len(stack), None), 200)


def calc(stack, operation):
    is_valid_op = Calculator.is_valid_op(operation)

    # Binary operation
    if is_valid_op == 2:
        return handle_stack_binary_op(stack, operation, is_valid_op)

    # Unary operation
    if is_valid_op == 1:
        return handle_stack_unary_op(stack, operation, is_valid_op)

    # No such operation
    else:
        return Response(hr.convert_to_json(None, "Error: unknown operation: " + str(operation)), status=409)


def handle_stack_binary_op(stack, operation, is_valid_op):
    if len(stack) >= 2:
        x = stack.pop()
        y = stack.pop()
        if operation == 'divide' and y == 0:  # Divide by zero is illegal
            return Response(hr.convert_to_json(None, "Error while performing operation Divide: division by 0"),
                            status=409)
        return Response(hr.convert_to_json(Calculator.calc_binary_op(operation, x, y), None), status=200)
    # Not enough arguments
    else:
        return Response(hr.convert_to_json(None, "Error: cannot implement operation " + str(operation) +
                                           ". It requires " + str(is_valid_op) + " arguments and the stack has only " +
                                           str(len(stack)) + " arguments"), status=409)


def handle_stack_unary_op(stack, operation, is_valid_op):
    if len(stack) >= 1:
        x = stack.pop()
        if x < 0 and operation == 'fact':
            return Response(hr.convert_to_json(None, "Error while performing operation Factorial: not supported for "
                                                     "the negative number"), status=409)
        return Response(hr.convert_to_json(Calculator.calc_unary_op(operation, x), None), status=200)
    # Not enough arguments
    else:
        return Response(hr.convert_to_json(None, "Error: cannot implement operation " + str(operation) +
                                           ". It requires " + str(is_valid_op) + " arguments and the stack has only " +
                                           str(len(stack)) + " arguments"), status=409)


# This function is for deleting some arguments from stack
def delete_arguments(stack, delete_body):
    args = int(delete_body['count'])
    if args <= len(stack):
        for i in range(args):
            stack.pop()
        return Response(hr.convert_to_json(len(stack), None), 200)
    return Response(hr.convert_to_json(None, "Error: cannot remove " + str(args) + " from the stack. It has only " +
                                       str(len(stack)) + " arguments"), status=409)
