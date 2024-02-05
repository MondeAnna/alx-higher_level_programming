#!/usr/bin/python3


"""
Rebel Integer
"""


class MyInt(int):
    """
    Rebel Integer
    """

    def __eq__(self, other):
        return self is other

    def __ne__(self, other):
        return not self.__eq__(other)
