#!/usr/bin/python3


def text_indentation(text):
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
