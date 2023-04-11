#!/usr/bin/python3
"""Module containing Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class. Inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width(int): Width of the rectangle.
            height(int): Height of the rectangle.
        """
        super().__init__()

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
