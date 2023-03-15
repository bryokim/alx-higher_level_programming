#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if a_dictionary:
        delete_keys = [key for key, value1 in a_dictionary.items()
                       if value1 == value
                       ]
        for key in delete_keys:
            del a_dictionary[key]

    return a_dictionary
