#!/usr/bin/python3


def weight_average(my_list=[]):
    average = 0
    if my_list:
        total_score = sum([item[0] * item[1] for item in my_list])
        total_weight = sum([item[1] for item in my_list])
        average = total_score / total_weight

    return average
