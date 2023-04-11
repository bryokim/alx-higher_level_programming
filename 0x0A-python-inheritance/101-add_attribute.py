#!/usr/bin/python3
"""Module containing add_attributa function"""


def add_attribute(obj, name, value):
    """Adds new attribute to an object if it's possible

    Args:
        obj (object): Object to add the new attribute to.
        name (str): Key to add to obj.__dict__
        value (str): Value to add to obj.__dict__

    Raises:
        TypeError: If obj does not have __dict__ attribute.
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
