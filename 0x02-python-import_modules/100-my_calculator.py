#!/usr/bin/python3

import calculator_1 as calc
import sys
from sys import argv

operators = ['+', '-', '*', '/']


def validate_num_args():
    """Checks whether number of arguments is 3.
    """
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)


def validate_operator(operator):
    """Checks whether given operator is valid.
    """
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


def perform_operation(a, b, operator):
    """Performs requested operation on a and b and prints
    the result.

    Args:
        a: first integer
        b: second integer
        operator: Indicates operation to be carried out
    """
    if operator == '+':
        result = calc.add(a, b)
    elif operator == '-':
        result = calc.sub(a, b)
    elif operator == '*':
        result = calc.mul(a, b)
    else:
        result = calc.div(a, b)

    print(f"{a} {operator} {b} = {result}")


if __name__ == "__main__":
    argv.pop(0)
    validate_num_args()
    a, op, b = [int(arg) if i % 2 == 0 else arg for i, arg in enumerate(argv)]
    validate_operator(op)
    perform_operation(a, b, op)
