#!/usr/bin/python3


""" Square Class; child of Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class; child of Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """ return implementation of repr for str() """

        x_y = f"{self.x}/{self.y}"
        return f"[Square] ({self.id}) {x_y} - {self.width}"
