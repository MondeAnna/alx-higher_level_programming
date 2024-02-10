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

    def area(self):
        """ provides an instances area """

        return self.width * self.height

    def display(self):
        """ display rectangle using hash characters """

        if self.y:
            print("\n" * self.y, end="")

        spaces = " " * self.x
        hashes = "#" * self.width

        for row in range(self.height):
            print(f"{spaces}{hashes}")

    @property
    def height(self):
        """ provide height of rectangle """

        return self.__height

    @height.setter
    def height(self, value):
        """
        set height of rectangle

        Parameter
        ---------
        value : int
            value to be assigned as height
        """

        self.__validate_int(value, "height")
        self.__validate_positive(value, "height")
        self.__height = value

    def to_dictionary(self):
        """ provide attribute/value pairs in dictionary """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }

    def update(self, *args, **kwargs):
        """
        update object attributes as per internal order,
        where `args` are provided, `kwargs` are ignored

        Parameters
        ----------
        args : int
        kwargs : int

        Internal Order
        --------------
        id : int
        width : int
        height : int
        x : int
        y : int
        """

        self.__update_args(*args)
        if not args:
            self.__update_kwargs(**kwargs)

    @property
    def width(self):
        """ provide width of rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """
        set width of rectangle

        Parameter
        ---------
        value : int
            value to be assigned as height
        """

        self.__validate_int(value, "width")
        self.__validate_positive(value, "width")
        self.__width = value

    @property
    def x(self):
        """ provide x of rectangle """

        return self.__x

    @x.setter
    def x(self, value):
        """
        set x of rectangle

        Parameter
        ---------
        value : int
            value to be assigned as height
        """

        self.__validate_int(value, "x")
        self.__validate_not_negative(value, "x")
        self.__x = value

    @property
    def y(self):
        """ provide y of rectangle """

        return self.__y

    @y.setter
    def y(self, value):
        """
        set y of rectangle

        Parameter
        ---------
        value : int
            value to be assigned as height
        """

        self.__validate_int(value, "y")
        self.__validate_not_negative(value, "y")
        self.__y = value

    def __update_args(self, *args):
        """
        update object attributes as per internal order

        Parameters
        ----------
        args : int

        Internal Order
        --------------
        id : int
        width : int
        height : int
        x : int
        y : int
        """

        if not args:
            return

        len_ = len(args)
        attrs = ("id", "width", "height", "x", "y")[:len_]

        for attr, arg in zip(attrs, args):
            self.__setattr__(attr, arg)

    def __update_kwargs(self, **kwargs):
        """
        update object attributes as pass kwargs

        Parameters
        ----------
        kwargs : int
        """

        for attr, arg in kwargs.items():
            self.__setattr__(attr, arg)

    def __validate_int(self, value, attr):
        """
        validate value is int

        Parameter
        ---------
        value : int
            value being validated
        attr : str
            name of attribute value is to be assigned to
        """

        if not isinstance(value, int):
            raise TypeError(f"{attr} must be an integer")

    def __validate_positive(self, value, attr):
        """
        validate value is positive

        Parameter
        ---------
        value : int
            value being validated
        attr : str
            name of attribute value is to be assigned to
        """

        if value <= 0:
            raise ValueError(f"{attr} must be > 0")

    def __validate_not_negative(self, value, attr):
        """ validate value is not negative

        Parameter
        ---------
        value : int
            value being validated
        attr : str
            name of attribute value is to be assigned to
        """

        if value < 0:
            raise ValueError(f"{attr} must be >= 0")

    def __str__(self):
        """ return implementation of repr for str() """

        return self.__repr__()

    def __repr__(self):
        """ repr base """

        x_y = f"{self.x}/{self.y}"
        width_height = f"{self.width}/{self.height}"
        return f"[Rectangle] ({self.id}) {x_y} - {width_height}"
