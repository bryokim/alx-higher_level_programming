#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    square_matrix = []
    for nums in matrix:
        nums_square = [num**2 for num in nums]
        square_matrix.append(nums_square)

    return square_matrix
