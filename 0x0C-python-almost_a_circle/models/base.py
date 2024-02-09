#!/usr/bin/python3


""" Base class """


class Base:

    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ where id is none, set id to current object count """

        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    def __del__(self):
        """ decrement object count upon destruction """

        Base.__nb_objects -= 1
