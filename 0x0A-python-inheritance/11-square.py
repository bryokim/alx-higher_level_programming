#!/usr/bin/python3
"""Module containing Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class. Inherits from the Rectangle class"""

    def __init__(self, size):
        """Initialize a Square instance. Inherits from Rectangle.

        Args:
            size (int): Size of the square.
        """
        super().__init__(size, size)
        self.__size = size
