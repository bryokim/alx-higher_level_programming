#!/usr/bin/python3
"""
Module that reads stdin and computes metrics and prints to stdout.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL-C) prints the statistics
since the beginning. See print_statistics function for printing format.
"""

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


def print_statistics(size, codes):
    """Prints details about metrics.

    Args:
        size (int): File size.
        codes (dict): Dictionary of status codes and the
                      number of times they occured.
    """
    print(f"File size: {size}")
    for key, value in codes.items():
        if value:   # Print <status code>: <number> if number is not 0.
            print(f"{key}: {value}")


def read_size_and_code(line: str):
    """Read file size and status code from line.

    Args:
        line (str): Line of text as red from stdin.

    Returns:
        tuple: Tuple of both size and code.
    """
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
    if size[0] == '\n':
        size = size[1:]
    return (size[-1::-1], code[-1::-1])


def compute_metrics():
    global file_size
    global status_codes
    line = sys.stdin.readline()
    counter = 0
    try:
        while line:
            size, code = read_size_and_code(line)

            file_size += int(size)
            status_codes[code] += 1

            counter += 1
            line = sys.stdin.readline()
            while line == '\n':  # Skip blank lines.
                line = sys.stdin.readline()

            if counter == 10 or not line:  # Print if counter is 10 or if EOF.
                print_statistics(file_size, status_codes)
                counter = 0
    except Exception as e:
        print_statistics(file_size, status_codes)
        sys.exit(f"[{e.__class__.__name__}]: {e}")
    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)


if __name__ == "__main__":
    compute_metrics()
