#!/usr/bin/python3
"""Module containing add_integer function for adding two integers.

Raises:
    TypeError: If any of the two values to be added is no an integer
        or float.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int): First integer.
        b (int, optional): Second integer. Defaults to 98.

    Raises:
        TypeError: If a or b is not a float or integer.

    Returns:
        int: Result of the addition.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
