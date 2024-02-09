#!/usr/bin/python3


""" Rectangle class """


from models.base import Base


class Rectangle(Base):
    """ Rectagle Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """ provide height of rectangle """

        return self.__height

    @height.setter
    def height(self, value):
        """ set height of rectangle """

        self.__height = value

    @property
    def width(self):
        """ provide width of rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ set width of rectangle """

        self.__width = value

    @property
    def x(self):
        """ provide x of rectangle """

        return self.__x

    @x.setter
    def x(self, value):
        """ set x of rectangle """

        self.__x = value

    @property
    def y(self):
        """ provide y of rectangle """

        return self.__y

    @y.setter
    def y(self, value):
        """ set y of rectangle """

        self.__y = value
