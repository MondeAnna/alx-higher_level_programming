#!/usr/bin/python3


"""
Rectangle Class
"""


class Rectangle:
    """
    Rectangle Class
    """

    number_of_instances = 0
    __print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def print_symbol(self):
        return self.__print_symbol

    @print_symbol.setter
    def print_symbol(self, value):
        self.__print_symbol = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    def area(self):
        """get area"""
        return self.height * self.width

    def perimeter(self):
        """get perimeter"""
        if not self.height or not self.width:
            return 0
        return self.height * 2 + self.width * 2

    def __str__(self):
        """get graphical representation"""
        str_ = ""
        symbol = str(self.print_symbol)
        if not self.height or not self.width:
            return str_
        for _ in range(self.height):
            str_ += symbol * self.width + "\n"
        return str_[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
