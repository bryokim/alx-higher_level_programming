#!/usr/bin/python3


def rem_common(common_set, my_set):
    return list(filter(lambda x: x not in common_set, my_set))


def only_diff_elements(set_1, set_2):
    common_set = [element for element in set_1 if element in set_2]
    diff_set = rem_common(common_set, set_1) + rem_common(common_set, set_2)
    return diff_set
