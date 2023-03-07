#!/usr/bin/python3

def fizzbuzz():
    for num in range(1, 101):
        var = ""

        if num % 3 == 0:
            var += "Fizz"
        if num % 5 == 0:
            var += "Buzz"

        if len(var):
            print(var, end=" ")
        else:
            print("{:d}".format(num), end=" ")
