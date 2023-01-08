import logging

import Calculator
from flask import Response
import HandleRequest as hr

stack_logger = hr.stack_logger


def stack_size(stack):
    stack_logger.info("Stack size is %d", len(stack))
    stack_logger.debug("Stack content (first == top): [" + ','.join(str(v) for v in reversed(stack)) + "]")
    return Response(hr.convert_to_json(len(stack), None), 200)


def add_arguments(stack, put_body):
    args = put_body['arguments']
    stack_size_before = len(stack)

    for i in args:
        if not isinstance(i, int):
            stack_logger.error("Server encountered an error ! message: Error: not all arguments are valid")
            return Response(hr.convert_to_json(None, "Error: not all arguments are valid"), 409)

    for i in args:
        stack.append(i)

    stack_logger.setLevel(logging.DEBUG)
    stack_logger.info("Adding total of %d argument(s) to the stack | Stack size: %d", len(args), len(stack))
    stack_logger.debug("Adding arguments: " + ','.join(str(a) for a in args) + " |"
                       " Stack size before %d | stack size after %d", stack_size_before, len(stack))
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
        stack_logger.error("Server encountered an error ! message: Error: unknown operation: " + str(operation))
        return Response(hr.convert_to_json(None, "Error: unknown operation: " + str(operation)), status=409)


def handle_stack_binary_op(stack, operation, is_valid_op):
    if len(stack) >= 2:
        x = stack.pop()
        y = stack.pop()

        # Divide by zero is illegal
        if operation == 'divide' and y == 0:
            return divide_by_zero()

        # Make operation
        val = Calculator.calc_binary_op(operation, x, y)

        stack_logger.info("Performing operation %s. Result is %d |"
                          " stack size: %d", operation, val, len(stack))
        stack_logger.debug("Performing operation: %s(%d,%d) = %d", operation, x, y, val)
        return Response(hr.convert_to_json(val, None), status=200)

    # Not enough arguments
    else:
        return not_enough_args(stack, operation, is_valid_op)


def divide_by_zero():
    stack_logger.error("Server encountered an error ! message:"
                       " Error while performing operation Divide: division by 0")
    return Response(hr.convert_to_json(None, "Error while performing operation Divide: division by 0"),
                    status=409)


def not_enough_args(stack, operation, is_valid_op):
    stack_logger.error("Server encountered an error ! message: "
                       "Error: cannot implement operation " + str(operation) +
                       ". It requires " + str(is_valid_op) +
                       " arguments and the stack has only " +
                       str(len(stack)) + " arguments")
    return Response(hr.convert_to_json(None, "Error: cannot implement operation " + str(operation) +
                                       ". It requires " + str(is_valid_op) + " arguments and the stack has only " +
                                       str(len(stack)) + " arguments"), status=409)


def handle_stack_unary_op(stack, operation, is_valid_op):
    if len(stack) >= 1:
        x = stack.pop()
        if x < 0 and operation == 'fact':
            return negative_fact()

        # Make operation
        val = Calculator.calc_unary_op(operation, x)

        stack_logger.info("Performing operation %s. Result is %d |"
                          " stack size: %d", operation, val, len(stack))
        stack_logger.debug("Performing operation: %s(%d) = %d", operation, x, val)

        return Response(hr.convert_to_json(val, None), status=200)


    # Not enough arguments
    else:
        return not_enough_args(stack, operation, is_valid_op)


def negative_fact():
    stack_logger.error("Server encountered an error ! message: Error while performing operation Factorial: not "
                       "supported for the negative number")
    return Response(hr.convert_to_json(None, "Error while performing operation Factorial: not supported for "
                                             "the negative number"), status=409)


# This function is for deleting some arguments from stack
def delete_arguments(stack, delete_body):
    args = int(delete_body['count'])
    if args <= len(stack):
        for i in range(args):
            stack.pop()
        stack_logger.info("Removing total %d argument(s) from the stack |"
                          " Stack size: %d", args, len(stack))
        return Response(hr.convert_to_json(len(stack), None), 200)
    stack_logger.error("Server encountered an error ! message: Error: cannot remove " + str(args) +
                       " from the stack. It has only " + str(len(stack)) + " arguments")
    return Response(hr.convert_to_json(None, "Error: cannot remove " + str(args) + " from the stack. It has only " +
                                       str(len(stack)) + " arguments"), status=409)
