#!/usr/bin/python3
"""Module containing add_item implementation"""

import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(filename):
    """Adds all arguments to a Python list and then saves them to a file

    Args:
        filename (str): Name of the file to save the list.
    """
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    items.extend(argv[1:])

    save_to_json_file(items, filename)


if __name__ == "__main__":
    add_item("add_item.json")
