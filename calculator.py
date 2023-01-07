import math

# This function check if the operation is valid
def is_valid_op(operation):
    if (operation == 'plus' or
            operation == 'minus' or
            operation == 'times' or
            operation == 'divide' or
            operation == 'pow'):
        return 2

    if (operation == 'abs' or
            operation == 'fact'):
        return 1
    return 0

# This function calculate binary operation
def calc_binary_op(operation, x, y):
    if (operation == 'plus'):
        return plus(x, y)
    if operation == 'minus':
        return minus(x, y)
    if operation == 'times':
        return times(x, y)
    if operation == 'divide':
        return divide(x, y)
    if operation == 'pow':
        return my_pow(x, y)
    return False

# This function calculate unary operation
def calc_unary_op(operation, x):
    if operation == 'abs':
        return my_abs(x)
    if operation == 'fact':
        return my_fact(x)

# operations implement:

def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def times(x, y):
    return x * y


def divide(x, y):
    return int(x / y)


def my_pow(x, y):
    return pow(x, y)


def my_abs(x):
    return abs(x)


def my_fact(x):
    return math.factorial(x)
