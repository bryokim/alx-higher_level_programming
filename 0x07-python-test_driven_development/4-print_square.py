#!/usr/bin/python3
"""Module that prints a square with the # character."""


def print_square(size):
    """Prints a square of length size using the # character.

    Args:
        size (int): Size of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size == 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
