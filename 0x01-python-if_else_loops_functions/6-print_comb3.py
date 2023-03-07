#!/usr/bin/python3

for i in range(0, 9):
    lower = (i * 10) + i + 1
    upper = (i + 1) * 10

    for j in range(lower, upper):
        if i != 8:
            print("{:02d},".format(j), end=" ")
        else:
            print("{:d}".format(j))
