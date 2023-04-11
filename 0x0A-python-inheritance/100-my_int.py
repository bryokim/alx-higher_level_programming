#!/usr/bin/python3
"""Module containing MyInt class"""


class MyInt(int):
    """MyInt class. Inherits from int"""

    def __init__(self, value):
        """Initialize a MyInt instance.

        Args:
            value (int): Value of the integer being assigned.
        """
        self.value = value

    def __ne__(self, other):
        """Check equallity of two integers.

        Args:
            other (int, class: MyInt): Integer or instance of MyInt
                to compare with current instance.

        Returns:
            bool: True if values are equal, or False if unequal.
        """
        if isinstance(other, MyInt):
            return self.value == other.value
        return self.value == other

    def __eq__(self, other):
        """Check inequality of two integers.

        Args:
            other (int, class: MyInt): Integer or instance of MyInt
                to compare with current instance.

        Returns:
            _type_: True if values are unequall, otherwise False.
        """
        if isinstance(other, MyInt):
            return self.value != other.value
        return self.value != other
