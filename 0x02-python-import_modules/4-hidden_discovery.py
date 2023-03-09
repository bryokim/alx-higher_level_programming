#!/usr/bin/python3

import hidden_4


def print_names():
    """Prints names in hidden_4 excluding those
    starting with __
    """
    for name in dir(hidden_4):
        if name[:2] != '__':
            print(name)


if __name__ == "__main__":
    print_names()
