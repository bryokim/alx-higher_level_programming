#!/usr/bin/python3
"""Module containing from_json_string function"""

import json


def from_json_string(my_str):
    """Returns an object(Python data structure) represented
    by a JSON string.

    Args:
        my_str (str): JSON string.

    Returns:
        object: Object from the JSON string.
    """
    return json.loads(my_str)
