#!/usr/bin/python3


""" A class defining a Square object """


class Square:

    """ square class """

    def __init__(self, size=0, position=(0, 0)):
        self.position = position
        self.size = size

    def area(self):
        return self.size ** 2

    def my_print(self):
        if not self.size:
            print()
            return

        n_space = self.__position[0]

        for row in range(self.size):
            print(end=" " * n_space)
            for col in range(self.size):
                print(end="#")
            print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__validate_position(value)
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__validate_size(value)
        self.__size = value

    def __validate_position(self, position):
        is_pair = len(position) == 2
        are_positive = all(n >= 0 for n in position)

        if not (is_pair and are_positive):
            raise TypeError("position must be a tuple of 2 positive integers")

    def __validate_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
