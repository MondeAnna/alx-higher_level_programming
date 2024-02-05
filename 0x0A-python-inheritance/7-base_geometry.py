#!/usr/bin/python3


"""
Empty class
"""


class BaseGeometry:
    """
    Empty class
    """

    def area(self):
        """
        Raises:
            Exception: occurs upon call
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        that validates value:

        Args:
            name: name
            value: value

        Raises:
            TypeError: value to be int
            ValueError: value to be greater than zero
        """

        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
