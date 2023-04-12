#!/usr/bin/python3
"""Module containing the implementation of the Student class"""


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

    def to_json(self, attrs=None):
        """Retrieves a dectionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to be retrieved.
                                    Defaults to None.

        Returns:
            dict: Dictionary representation of Student instance.
        """
        if not attrs:
            return self.__dict__

        new_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                new_dict[attr] = self.__dict__[attr]
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing attributes and values
                         as key/value pairs
        """
        for key, value in json.items():
            self.__dict__[key] = value
