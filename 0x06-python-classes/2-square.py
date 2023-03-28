#!/usr/bin/python3
"""This module contains Square class.

Raises:
    ValueError: If size of the square is negative.
    TypeError: If size of the square is not an integer.
"""


def check_size(size):
    """Validate size of square

    Args:
        size(int): The size of the square.

    Raises:
        TypeError: If size of the square is not an integer.
        ValueError: If size of the square is negative.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")


class Square:
    """Square class that defines a square"""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            ValueError: If size is negative.
            TypeError: If size is not an integer.
        """
        check_size(size)
        self.__size = size
