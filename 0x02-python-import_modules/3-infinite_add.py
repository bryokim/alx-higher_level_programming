#!/usr/bin/python3

from sys import argv


def sum_of_args():
    """Prints sum of arguments passed"""
    sum = 0
    argv.pop(0)
    for arg in argv:
        sum += int(arg)

    print(f"{sum}")


if __name__ == "__main__":
    sum_of_args()
