#!/usr/bin/python3
"""Module containing Student class implementation"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of Student.

        Args:
            first_name (str): First name.
            last_name (str): Last name.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dectionary representation of a Student instance.

        Returns:
            dict: Dictionary representation of a Student instance.
        """

        return self.__dict__
