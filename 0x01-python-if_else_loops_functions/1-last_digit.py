#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str = "Last digit of {:d} is ".format(number)
last_digit = abs(number) % 10

if number < 0 and last_digit != 0:
    str += "-{:d} ".format(last_digit)
else:
    str += "{:d} ".format(last_digit)


if last_digit > 5:
    str += "and is greater than 5"
elif last_digit == 0:
    str += "and is 0"
else:
    str += "and is less than 6 and not 0"

print(str)
