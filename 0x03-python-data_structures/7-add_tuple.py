#!/usr/bin/python3

def new_tuple(tp, len_tp):
    if len_tp == 0:
        return (0, 0)
    else:
        return (tp[0], 0)


def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a < 2:
        tuple_a = new_tuple(tuple_a, len_a)
    if len_b < 2:
        tuple_b = new_tuple(tuple_b, len_b)

    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]

    return (sum_1, sum_2)
