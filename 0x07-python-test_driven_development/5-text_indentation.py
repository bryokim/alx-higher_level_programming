#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after each of these characters:
    . or ? or :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after . or ? or :

    Args:
        text (str): Tex to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]
    sign = 0

    for i in text:
        if not sign:
            print(i, end="")
            if i in chars:
                print("\n")
                sign = 1
        else:
            if i == " " or i == "\t":
                pass
            else:
                print(i, end="")
                sign = 0
