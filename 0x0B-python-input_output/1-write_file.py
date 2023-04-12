#!/usr/bin/python3
"""Module containing write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number of
    characters written.
    It ovewrites the file if it exists and cretes the file if
    it does not exist.

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        text (str, optional): Text to be written into file. Defaults to "".

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding='utf-8') as f:
        num = f.write(text)
    return num
