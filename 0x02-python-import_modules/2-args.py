#!/usr/bin/python3

from sys import argv

number_of_args = len(argv)


def print_args(num_arg):
    """Prints arguments passed to program

    Args:
        num_arg: Number of arguments

    """
    str = ""
    if num_arg == 1:
        str = "0 arguments."
    elif num_arg == 2:
        str = "1 argument:"
    else:
        str = f"{num_arg - 1} arguments:"

    print(str)

    """Remove program name as it's not to be printed"""
    argv.pop(0)
    for idx, arg in enumerate(argv, start=1):
        print(f"{idx}: {arg}")


if __name__ == "__main__":
    print_args(number_of_args)
