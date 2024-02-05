#!/usr/bin/python3


"""
Attribute adder
"""


def add_attribute(cls, name, value):
    """
    Attribute adder
    """
    if cls.__class__.__name__ in dir(__builtins__):
        raise TypeError("can't add new attribute")
    cls.__setattr__(name, value)
