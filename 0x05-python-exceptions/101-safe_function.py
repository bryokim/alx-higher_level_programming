#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fun_c = fct(*args)
        return fun_c
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
