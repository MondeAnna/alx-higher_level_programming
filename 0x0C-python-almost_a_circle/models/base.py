#!/usr/bin/python3


""" Base class """


import json


class Base:

    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ where id is none, set id to current object count """

        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ provide json string of object """

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    def __del__(self):
        """ decrement object count upon destruction """

        Base.__nb_objects -= 1
