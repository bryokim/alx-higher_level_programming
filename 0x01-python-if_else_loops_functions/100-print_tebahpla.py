#!/usr/bin/python3

for letter in range(ord('z'), ord('a') - 1, -1):
    if letter % 2 == 0:
        print("{:c}".format(letter), end="")
    else:
        letter = letter - ord('a') + ord('A')
        print("{:c}".format(letter), end="")
