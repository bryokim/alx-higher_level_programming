#!/usr/bin/python

def print_alphabet():
    """Prints the alphabet in uppercase
    """
    for letter in range(ord('A'), ord('Z') + 1):
        print(f"{letter:c}", end="")
    print("")
