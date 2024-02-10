#!/usr/bin/python3


""" Square Class; child of Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class; child of Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """ provide the size of a side of a square """

        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """
        set size of square

        Parameter
        ---------
        value : int
            value to be assigned as size
        """

        self.width = value
        self.height = value

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
            self._Rectangle__update_kwargs(**kwargs)

    def __update_args(self, *args):
        """
        update object attributes as per internal order

        Parameters
        ----------
        args : int

        Internal Order
        --------------
        id : int
        size : int
        x : int
        y : int
        """

        if not args:
            return

        len_ = len(args)
        attrs = ("id", "size", "x", "y")[:len_]

        for index, attr, arg in zip(range(len_), attrs, args):
            self.__setattr__(attr, arg)

    def __str__(self):
        """ return implementation of repr for str() """

        x_y = f"{self.x}/{self.y}"
        return f"[Square] ({self.id}) {x_y} - {self.width}"
