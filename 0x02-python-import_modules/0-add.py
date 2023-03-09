#!/usr/bin/python3

from add_0 import add

a = 1
b = 2


def find_sum(a, b):
    return add(a, b)


if __name__ == "__main__":
    result = find_sum(a, b)
    print("{} + {} = {}".format(a, b, result))
