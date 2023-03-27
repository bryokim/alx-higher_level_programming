#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: ", end="")
        if result is not None:
            print(f"{result:.1f}")
        else:
            print("None")
    return result
