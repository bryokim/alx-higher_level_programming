#!/usr/bin/python3
"""
Module that reads stdin and computes metrics and prints to stdout.

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL-C) prints the statistics
since the beginning. See print_statistics function for printing format.
"""

import sys
import re

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


def get_size_and_code_nonstrict(line: str):
    """
    Read file size and status code from line.

    Reads the file size and code non-sparingly provided line is a
    valid string.\n
    Does not check validity of the file size or status code.\n
    That is whether file size is an integer between 1 and 1024(exclusive) or
    whether status code is found in status_codes dictionary.

    Therefore extra checks must be done on the values returned from this
    function to check their validity before being used.

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
    return (code[-1::-1], size[-1::-1])


def get_size_and_code_strict(line):
    """
    Strictly matches the segment of line with the regex of the format
    required.\n
    This function is not used in matching the line since it skips lines which
    don't exactly adhere to the format or don't contain a portion that does.\n
    It can be used if format of lines being read is strictly required to
    follow the format.

    Format:\n
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" \
<status code> <file size>

        File size => 1 - 1024(exclusive)
        Status codes => [200, 301, 400, 401, 403, 404, 405, 500]

    The following lines pass the search:\n
        128.230.61.246 - [2017-02-05 23:31:23.258076] \
"GET /projects/260 HTTP/1.1" 301 292\n
        8.20.161.246 - [2013-01-05 23:31:23.138174] \
"GET /projects/260 HTTP/1.1" 400 1023\n
        18.0.1.2 - [2022-10-02 24:35:33.258076] \
"GET /projects/260 HTTP/1.1" 500 1

    Args:
        line (str): Line to search in.

    Returns:
        tuple: Tuple containing the file size and status code from the
                matched line if found or empty strings if not successfuly
                matched.
    """
    single_value = r"[01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]"
    ip = r"({0}[.]{0}[.]{0}[.]{0})".format(single_value)
    date = r"\[(\d){4}-(\d){2}-(\d){2} ((\d){2}:){2}(\d){2}.(\d){6}\]"
    string = r"\"GET /projects/260 HTTP/1.1\""
    status_code = r"(200|301|400|401|403|404|405|500)"
    file_size = r"(10[0-2][0-3]|[1-9][0-9][0-9]|[1-9][0-9]|[1-9])"

    lineRegex = re.compile(f"{ip} - {date} {string} {status_code} {file_size}")

    try:
        mo = lineRegex.search(line)
        return mo.group(9, 10)
    except AttributeError:
        return ("", "")


def compute_metrics():
    """
    Main function that reads, computes and prints metrics.
    """
    global file_size
    global status_codes
    line = sys.stdin.readline()
    counter = 0
    try:
        while line:
            code, size = get_size_and_code_nonstrict(line)
            # For strict matching instead use:
            # code, size = get_size_and_code_strict(line)

            try:
                file_size += int(size)
                if code in status_codes:
                    status_codes[code] += 1
                counter += 1
            except ValueError:
                pass    # If size can not be converted to int.

            line = sys.stdin.readline()
            while line == '\n':  # Skip blank lines.
                line = sys.stdin.readline()

            if counter == 10 or not line:  # Print if counter is 10 or if EOF.
                print_statistics(file_size, status_codes)
                counter = 0
            code, size = ("", "")
    except KeyboardInterrupt:
        print_statistics(file_size, status_codes)

    if not file_size:   # If file is empty.
        print("File size: 0")


if __name__ == "__main__":
    compute_metrics()
