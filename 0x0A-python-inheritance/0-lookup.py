#!/usr/bin/python3
"""Module containing lookup function"""


def lookup(obj):
    """Returns the list of available attributes and
    methods of an object.

    Args:
        obj (object): Object to look into.

    Returns:
        list: List of attributes and methods.
    """
    return dir(obj)
