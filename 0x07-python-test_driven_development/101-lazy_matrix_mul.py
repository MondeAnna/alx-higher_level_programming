#!/usr/bin/python3


"""
Lazy matrix multiplication
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices by using the module NumPy
    """

    validate_matrices(m_a, m_b)
    return np.matmul(m_a, m_b)


def validate_matrices(m_a, m_b):
    _validate_shell(m_a, "m_a")
    _validate_shell(m_b, "m_b")

    _validate_rows(m_a, "m_a")
    _validate_rows(m_b, "m_b")

    _validate_not_empty(m_a, "m_a")
    _validate_not_empty(m_b, "m_b")

    _validate_numbers(m_a, "m_a")
    _validate_numbers(m_b, "m_b")

    _validate_is_rectangle(m_a, "m_a")
    _validate_is_rectangle(m_b, "m_b")

    _validate_multipllicability(m_a, m_b)


def _validate_shell(var, var_name):
    if not isinstance(var, list):
        raise TypeError(f"{var_name} must be a list")


def _validate_rows(var, var_name):
    for row in var:
        if not isinstance(row, list):
            raise TypeError(f"{var_name} must be a list of lists")


def _validate_not_empty(var, var_name):
    if set(map(len, var)) in [set(), {0}]:
        raise ValueError(f"{var_name} can't be empty")


def _validate_numbers(var, var_name):
    message = f"{var_name} should contain only integers or floats"
    for row in var:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(message)


def _validate_is_rectangle(var, var_name):
    message = f"each row of {var_name} must be of the same size"
    lengths = map(len, var)
    unique_lengths = set(lengths)
    if len(unique_lengths) != 1:
        raise TypeError(message)


def _validate_multipllicability(m_a, m_b):
    ncol = len(m_a[0])
    nrow = len(m_b)

    if ncol != nrow:
        raise ValueError("m_a and m_b can't be multiplied")
