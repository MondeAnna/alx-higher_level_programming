#!/usr/bin/python3


"""
a function that print: My name is <first name> <last name>
>>> say_my_name("Amanda", "Bavu")
My name is Amanda Bavu
"""


def say_my_name(first_name, last_name=""):
    """
    a function that print:
        My name is <first name> <last name>
    """

    _validate_var(first_name, "first_name")
    _validate_var(last_name, "last_name")

    print("My name is {} {}".format(first_name, last_name))


def _validate_var(var, var_name):
    if not isinstance(var, str):
        raise TypeError(f"{var_name} must be a string")
