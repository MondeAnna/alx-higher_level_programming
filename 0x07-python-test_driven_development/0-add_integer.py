#!/usr/bin/python3

"""
add two integers
>>> add_integer(0, 0)
0
"""


def add_integer(a, b=98):
    """
    add two integers
    """

    _check_type(a, "a")
    _check_type(b, "b")

    a_int = _make_int(a, "a")
    b_int = _make_int(b, "b")

    return a_int + b_int


def _check_type(var, var_name):
    if type(var) not in [int, float]:
        raise TypeError(f"{var_name} must be an integer")


def _make_int(var, var_name):
    try:
        return int(var)
    except OverflowError:
        raise OverflowError(
            f"cannot convert float infinity {var_name} to integer"
        )
