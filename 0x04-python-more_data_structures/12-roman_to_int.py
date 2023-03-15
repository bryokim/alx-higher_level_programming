#!/usr/bin/python3

roman_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(roman_string):
    integer = 0
    if not roman_string or roman_string is None:
        return integer

    roman_string = roman_string.upper()
    for current, next in zip(roman_string, roman_string[1:]):
        current_value = roman_values.get(current)
        next_value = roman_values.get(next)

        if current_value < next_value:
            integer -= current_value
        else:
            integer += current_value

    # Add last roman since zip stops at second last
    integer += roman_values.get(roman_string[-1])

    return integer
