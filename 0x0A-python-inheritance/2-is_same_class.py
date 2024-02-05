#!/usr/bin/python3


"""
Determine if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Determine if an object is an instance of a class
    """
    return isinstance(obj, a_class) and a_class is not object
