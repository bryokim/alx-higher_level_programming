#!/usr/bin/python3
"""This module contains Square class.

Raises:
    ValueError: If size of the square is negative.
    TypeError: If size of the square is not an integer or
        or if the position is not a tuple of 2 positive integers.
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


def check_position(position):
    """Validate position of square

    Args:
        position (tuple): position of square.

    Raises:
        TypeError: If position is not a tuple or
            if len of position is not 2 or
            if any of the integers in the tuple is negative.
    """

    error_msg = "position must be a tuple of 2 positive integers"
    if not isinstance(position, tuple) or len(position) != 2:
        raise TypeError(error_msg)
    if position[0] < 0 or position[1] < 0:
        raise TypeError(error_msg)


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square class.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Position of the square

        Raises:
            ValueError: If value is negative.
            TypeError: If value is not an integer or
                if position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position of the square.

        The position setter method raises the following errors.
        Raises:
            TypeError: If position is not a tuple of 2 positive integers.

        Returns:
            tuple: Position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        check_position(value)
        self.__position = value

    def my_print(self):
        """Print the square with the character #"""
        if self.__size == 0:
            print("")

        for x in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")
