#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    upper_range = -(len(my_list) + 1)
    for i in range(-1, upper_range, -1):
        print("{}".format(my_list[i]))
