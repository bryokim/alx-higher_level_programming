#!/usr/bin/python3
"""Module containing class_to_json implementation"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structures
    for JSON serialization of an object.

    Args:
        obj (object: class): An instance of a class.

    Returns:
        dict: Dictionary description of obj.
    """
    return obj.__dict__
