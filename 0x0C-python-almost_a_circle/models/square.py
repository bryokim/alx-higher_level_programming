#!/usr/bin/python3
"""
Implementation of the Square class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Square class. Inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square.

        The setter raises following exceptions.
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def _update(self, new_values):
        """
        Helper function for update.

        Args:
            new_values (list): List of tuples each containing an attribute
                  and a new value to be assigned.
        """
        for attr, value in new_values:
            if attr == "size":
                self.size = value
            else:
                setattr(self, attr, value)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Variable length argument list.
            **kwargs: Keyword arguments.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            self._update(zip(attrs, args))
        else:
            self._update(kwargs.items())

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.

        Returns:
            dict: The dictionary representation of the square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }

    def __str__(self):
        """Get the string representation of the square.

        Format:
            [Class name] (<id>) <x>/<y> - <size>

        Returns:
            str: The string representation of the square.
        """
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x,
            self.y, self.width
        )
