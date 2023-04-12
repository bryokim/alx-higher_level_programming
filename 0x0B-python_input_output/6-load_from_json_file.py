#!/usr/bin/python3
"""Module containing load_from_json_file function"""

import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename (str): Name of the file.

    Returns:
        object: Python object fron the JSON file.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
