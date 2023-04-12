#!/usr/bin/python3
"""Module containing read_file function"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.

    Args:
        filename (str, optional): Name of the file. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
