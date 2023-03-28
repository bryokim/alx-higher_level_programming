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
    """Square class"""
    def __init__(self, size=0):
        """Initialize Square class.

        Args:
            size (int, optional): Size of the square. Defaults to 0.

        Raises:
            ValueError: If value is negative.
            TypeError: If value is not an integer.
        """
        self.size = size

    def area(self):
        """Calculate area of square

        Returns:
            int: The area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieves size of square

        The setter sets the size of the square.
        Raises:
            ValueError: If size is negative
            TypeError: If size is not integer

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        check_size(value)
        self.__size = value

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print("")

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
