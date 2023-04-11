#!/usr/bin/python3
"""Module containing MyList class"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """Prints the list sorted in an ascending order"""

        print(sorted(self))
