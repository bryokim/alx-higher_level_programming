#!/usr/bin/python3
"""
Module containing the rectangle class.

Raises:
    ValueError: If the height or width is less than zero.
    TypeError: If the height or width is no an integer.
"""


def check_value(value, name):
    """Check whether vale given is valid.

    Args:
        value (int): Value of either height or width.
        name (str): Name of the dimension being assigned value.

    Raises:
        ValueError: If the height or width is less than zero.
        TypeError: If the height or width is no an integer.
    """
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be >= 0")


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle objet.

        Args:
            width (int, optional): Width of the rectangle Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve width of the rectangle.

        The width setter raises folloeing errors:
            ValueError: If the height or width is less than zero.
            TypeError: If the height or width is no an integer.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        check_value(value, "width")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle.

        The setter raises the following errors:
            ValueError: If the height or width is less than zero.
            TypeError: If the height or width is no an integer.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        check_value(value, "height")
        self.__height = value

    def area(self):
        """Find area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Find the perimeter of the rectangle.

        Returns:
            int: 0 if width or height is 0, otherwise perimeter is calculated.
        """
        if not self.__width or not self.__height:
            return 0
        else:
            return self.__height * 2 + self.__width * 2
