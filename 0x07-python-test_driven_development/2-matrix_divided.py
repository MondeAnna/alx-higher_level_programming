#!/usr/bin/python3

"""
matrix division

>>> matrix_n_rows = [[1, 2, 3], [4, 5, 6]]
>>> div_negative = -17
>>>
>>> matrix_divided(matrix_n_rows, div_negative)
[[-0.06, -0.12, -0.18], [-0.24, -0.29, -0.35]]
>>>
>>> matrix_n_rows
[[1, 2, 3], [4, 5, 6]]
"""


def matrix_divided(matrix, div):
    """
    matrix division
    """

    if not matrix:
        return []

    _validate_matrix(matrix)
    _validate_div(div)

    return [
        [_division(n, div) for n in row]
        for row in matrix
    ]


def _division(num, div):
    return round(num / div, 2)


def _validate_div(div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")


def _validate_matrix(matrix):
    _assert_type(matrix)
    _assert_size(matrix)


def _assert_size(matrix):
    lengths = map(len, matrix)
    unique_lengths = set(lengths)
    if len(unique_lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")


def _assert_type(matrix):
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(message)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(message)

        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(message)
