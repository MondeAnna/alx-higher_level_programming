#!/usr/bin/python3


""" A class defining a Square object """


class Square:

    """ square class """

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__validate_size(value)
        self.__size = value

    def __validate_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return self.size > other.size

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)
