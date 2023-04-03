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

    # Count of number of instances of Rectangle.
    number_of_instances = 0
    # Character(s) used in printing string representation of the rectangle.
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle objet.

        Args:
            width (int, optional): Width of the rectangle Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Prints a the rectangle with the character(s) in print_symbol.

        Returns:
            str: Empty string if eiter height or width is zero, or
                last row of the rectangle.
        """
        str = ""
        if not self.__height or not self.__width:
            return str

        for h in range(self.__height):
            for w in range(self.__width):
                str += f"{self.print_symbol}"
            if h != self.__height - 1:
                str += "\n"
        return str

    def __repr__(self):
        """Return string representaion of the rectangle that can be used
        to recreate a new instance using eval().

        Returns:
            str: String representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns biggest rectangle based on area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            (obj:Rectangle): Biggest rectangle, or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns new Rectangle instance wit width == height == size

        Returns:
            (obj:Rectangle): new Rectangle of both width and height of size.
        """
        return cls(size, size)
