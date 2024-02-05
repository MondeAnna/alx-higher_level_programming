#!/usr/bin/python3


"""
Determine if an object is an instance of a class or its parent
"""


def is_kind_of_class(obj, a_class):
    """
    Determine if an object is an instance of a class or its parent
    """
    is_instance = isinstance(obj, a_class)
    is_subclass = issubclass(type(obj), object)
    return is_instance and is_subclass
