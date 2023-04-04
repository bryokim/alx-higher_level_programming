#!/usr/bin/python3
"""Module containing matrix_divided function thet divides a
matrix of integers/floats by a given number
"""


def matrix_divided(matrix, div):
    """Divides a matrix by given number.

    Args:
        matrix (list): List of lists of integers/floats.
        div (int/float) : Number to divide with the elements of the matrix.

    Raises:
        TypeError:
            If div is not an integer or float.
            If an element of matrix is not integer or float.
            If rows of matrix are not of same size.

        ZeroDivisionError: If div == 0.

    Returns:
        list: matrix wit all its elements divided by div.
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = len(matrix[0])
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError(err_msg)

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return m
