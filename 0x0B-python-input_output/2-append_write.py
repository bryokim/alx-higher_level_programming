#!/usr/bin/python3
"""Module contains append_write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    and returns number of characters added.

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        text (str, optional): Text to be added. Defaults to "".

    Returns:
        int: Number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        num = f.write(text)
    return num
