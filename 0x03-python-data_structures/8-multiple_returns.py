#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    first_char = ""

    if length != 0:
        first_char = sentence[0]
    else:
        first_char = None

    return (length, first_char)
