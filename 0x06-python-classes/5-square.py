#!/usr/bin/python3


""" A class defining a Square object """


class Square:

    """ square class """

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size ** 2

    def my_print(self):
        if not self.size:
            print()
            return

        for row in range(self.size):
            for col in range(self.size):
                print(end="#")
            print()

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
