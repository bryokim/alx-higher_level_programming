#!/usr/bin/python3

import calculator_1 as calc

a = 10
b = 5


def perform_operations(a: int, b: int):
    """Prints various operations on a and b

    Args:
        a: first integer
        b: second integer

    """
    print("{} + {} = {}".format(a, b, calc.add(a, b)))
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))
    print("{} / {} = {}".format(a, b, calc.div(a, b)))


if __name__ == '__main__':
    perform_operations(a, b)
