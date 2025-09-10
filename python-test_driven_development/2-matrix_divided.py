#!/usr/bin/python3
"""Utility library for matrix division

Provides a function for dividing matrices
check for invalid matrices and dividend
"""


def matrix_divided(matrix, div):
    """Divide a matrix with div

    Args:
        matrix: list of list int, float
        div: float, int

    Returns:
        matrix: new matrix with divided numbers

    Raises:
        TypeError: if matrix is not a matrix
        TypeError: if div is not float or int
        ZeroDivisionError: if div is 0
    """
    # check for valid matrix types
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) "
            "of integers/floats"
        )
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, (float, int)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

    # check for valid div
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in matrix:
        new_matrix.append([round(x / div, 2) for x in i])

    return new_matrix
