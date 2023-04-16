#!/usr/bin/python3
"""
Implementation of the Rectangle class.
"""
from .base import Base


class Rectangle(Base):
    """Rectangle class. Inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x coordinate of the rectangle.
                                Defaults to 0.
            y (int, optional): The y coordinate of the rectangle.
                                Defaults to 0.
            id (int, optional): The id of the instance. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle.

        The setter raises following exceptions.
        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than or equal to 0.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        The setter raises following exceptions.
        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than or equal to 0.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle.

        The setter raises following exceptions.
        Raises:
            TypeError: If the x coordinate is not an integer.
            ValueError: If the x coordinate is less than 0.

        Returns:
            int: The x coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle.

        The setter raises following exceptions.
        Raises:
            TypeError: If the y coordinate is not an integer.
            ValueError: If the y coordinate is less than 0.

        Returns:
            int: The y coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Get the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using the # character."""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Get the string representation of the rectangle.

        Format:
            [Class name] (<id>) <x>/<y> - <width>/<height>

        Returns:
            str: The string representation of the rectangle.
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.__x,
            self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Variable length argument list.
            **kwargs: Keyword arguments.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle.

        Returns:
            dict: The dictionary representation of the Rectangle.
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y,
        }
