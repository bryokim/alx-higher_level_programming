#!/usr/bin/python3
"""pascal_triangle implementation"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal's triangle.

    Args:
        n (int): Size of the Pascal's triangle.

    Returns:
        list: List of lists of Pascal triangle integers.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n + 1):
        if not i:
            continue

        nums = [1]
        if i > 2:
            for num1, num2 in zip(prev, prev[1:]):
                nums.append(num1 + num2)

        if i > 1:
            nums.append(1)
            prev = nums

        triangle.append(nums)

    return triangle
