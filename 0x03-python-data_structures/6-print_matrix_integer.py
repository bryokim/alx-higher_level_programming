#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for nums in matrix:
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end=" ")
        print("")
