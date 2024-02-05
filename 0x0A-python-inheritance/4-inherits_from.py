#!/usr/bin/python3


"""
Determine if object is from a subclass
"""


def inherits_from(obj, a_class):
    """
    Determine if object is from a subclass
    """
    type_ = type(obj)
    return type_ is not a_class and issubclass(type_, a_class)
