#!/usr/bin/python3
"""Module containing is_same_class function"""


def is_same_class(obj, a_class):
    """Checks whether an object is exactly an instance of specified
    class.

    Args:
        obj (object): Object to check.
        a_class (class): Class to compare to.

    Returns:
        bool: True if obj is exactly an instance of a_class,
                otherwise False.
    """
    return type(obj) is a_class  # obj.__class__ is a_class
