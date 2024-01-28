#!/usr/bin/python3


"""
Print square

>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    Print square
    """

    _validate_type(size)
    _validate_value(size)

    for row in range(size):
        print("#" * size)


def _validate_value(size):
    if size < 0:
        raise TypeError("size must be >= 0")


def _validate_type(size):
    message = "size must be an integer"

    if isinstance(size, float) and size < 0:
        raise TypeError(message)

    if not isinstance(size, int):
        raise TypeError(message)
