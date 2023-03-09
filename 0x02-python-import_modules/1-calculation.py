#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5


def perform_operations(a: int, b: int):
    """Prints various operations on a and b

    Args:
        a: first integer
        b: second integer

    """
    print("{} + {} = {:d}".format(a, b, add(a, b)))
    print("{} - {} = {:d}".format(a, b, sub(a, b)))
    print("{} * {} = {:d}".format(a, b, mul(a, b)))
    print("{} / {} = {:d}".format(a, b, div(a, b)))


if __name__ == "__main__":
    perform_operations(a, b)
