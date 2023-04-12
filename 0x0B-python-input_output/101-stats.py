#!/usr/bin/python3
"""Module that computes metrics"""

import sys

file_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0,
}


def print_details(size, codes):
    """Prints details about metrics.

    Args:
        size (int): File size.
        codes (dict): Dictionary of status codes and the
                      number of times they occured.
    """
    print(f"File size: {size}")
    for key, value in codes.items():
        if value:
            print(f"{key}: {value}")


line = sys.stdin.readline()
counter = 0
try:
    while line:
        size = ""
        code = ""
        i = 0
        for char in reversed(line):
            if char == ' ':
                i += 1
            elif not i:
                size += char
            elif i:
                code += char

            if i == 2:
                break
        file_size += int(size[1:])
        status_codes[code[-1::-1]] += 1
        line = sys.stdin.readline()
        counter += 1

        if counter % 10 == 0:
            print_details(file_size, status_codes)
except KeyboardInterrupt:
    print_details(file_size, status_codes)
