#!/usr/bin/python3
"""
Module fo multiplying two matrices.

    Raises:
        TypeError:
                If matrix is not a list, or
                If matrix is not a list of lists, or
                If an element is not an integer/float, or
                If rows of matrix differ in size.
        ValueError:
                If matrix is empty, or
                If the matrices can't be multiplied.

    Returns:
        list: Product of the two matrices given.
"""


class MatrixTests:
    """Class containing testing methods for matrices"""

    def __init__(self, name, matrix):
        """Initialize matrix.

        Args:
            name (str): Name of the matrix.
            matrix (list): The matrix itself
        """
        self.name = name
        self.matrix = matrix

    def get_test(self, idx):
        """Get test to be done.

        Args:
            idx (int): Index of the test

        Returns:
            (obj: method): Test o be run.
        """
        tests = [
            self.test_list(),
            self.test_list_of_lists(),
            self.test_empty(),
            self.test_elements_int_float(),
            self.test_is_rectangle(),
        ]
        return tests[idx]

    def test_list(self):
        """Test whether matrix is a list.

        Raises:
            TypeError: If matrix is not a list.
        """
        if not isinstance(self.matrix, list):
            raise TypeError(f"{self.name} must be a list")

    def test_list_of_lists(self):
        """Test whether matrix is a list of lists.

        Raises:
            TypeError: If matrix is not a list of lists.
        """
        for i in self.matrix:
            if not isinstance(i, list):
                raise TypeError(f"{self.name} must be a list of lists")

    def test_empty(self):
        """Test whether matrix is empty.

        Raises:
            ValueError: If matrix is empty.
        """
        if self.matrix == [] or self.matrix == [[]]:
            raise ValueError(f"{self.name} can't be empty")

    def test_elements_int_float(self):
        """Check whether all elements are integers/floats.

        Raises:
            TypeError: If an element is not an integer/float.
        """
        for i in self.matrix:
            for val in i:
                if not isinstance(val, int) and not isinstance(val, float):
                    raise TypeError(
                        f"{self.name} should contain only integers or floats"
                    )

    def test_is_rectangle(self):
        """Test whether rows of the matrix are of same size.

        Raises:
            TypeError: If rows differ in size.
        """
        size = len(self.matrix[0])
        for i in self.matrix:
            if size != len(i):
                raise TypeError(
                    f"each row of {self.name} must be of the same size"
                )


def test_matrices(names, matrices):
    """Test matrices.

    Args:
        names (list): List of names of matrices to test.
        matrices (list): List of matrices to be tested.
    """
    test_objs = [
        MatrixTests(name, matrix)
        for (name, matrix) in zip(names, matrices)
    ]

    test_objs[0].test_list()
    test_objs[1].test_list()
    test_objs[0].test_list_of_lists()
    test_objs[1].test_list_of_lists()
    test_objs[0].test_empty()
    test_objs[1].test_empty()
    test_objs[0].test_elements_int_float()
    test_objs[1].test_elements_int_float()
    test_objs[0].test_is_rectangle()
    test_objs[1].test_is_rectangle()


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Raises:
        ValueError: If the matrices can't be multiplied.

    Returns:
        list: Product of the two matrices.
    """
    test_matrices(["m_a", "m_b"], [m_a, m_b])

    result = []
    for list_a in m_a:
        sum_list = []
        # Loop for all columns in m_b
        for i in range(len(m_b[0])):
            try:
                # List of the products of matching elements.
                mul_list = [val * m_b[j][i] for j, val in enumerate(list_a)]
            except IndexError:
                raise ValueError("m_a and m_b can't be multiplied")
            """
            List of sums of the products of a single row in m_a
            with all the columns of m_b
            """
            sum_list.append(sum(mul_list))
        result.append(sum_list)
    return result
