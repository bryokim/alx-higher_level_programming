#!/usr/bin/python3
"""Module containing BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """Raise an exception.

        Raises:
            Exception: Always.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates an integer.

        Args:
            name (str): String to be assigned value.
            value (int): The integer being validated.

        Raises:
            TypeError: If value is not a integer.
            ValueError: If value is not greater then zero.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
