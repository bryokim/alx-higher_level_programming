#!/usr/bin/python3
"""append_after implementation"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        search_string (str, optional): String to search for. Defaults to "".
        new_sting (str, optional): String to add. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines_iter = iter(lines)
    index = 1
    while True:
        try:
            line = next(lines_iter)
            if search_string in line:
                lines.insert(index, new_string)
                next(lines_iter)
                index += 1
        except StopIteration:
            break
        index += 1

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
