#!/usr/bin/python3
"""Module containing inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that inherited
    (directly or indirectly) from a_class.

    Args:
        obj (object): Object to check.
        a_class (class): Class to compare to.

    Returns:
        bool: True if obj is a subclass of a_class, otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
