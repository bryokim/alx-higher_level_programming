#!/usr/bin/python3
"""Module containing is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Checks whether obj is an instance of a_class or instance of a
    class that inherited from a_class.

    Args:
        obj (object): Object to check.
        a_class (class): Classt compare to.

    Returns:
        bool: True if obj is instance of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
