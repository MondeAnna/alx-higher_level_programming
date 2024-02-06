#!/usr/bin/python3


"""
Student class section
"""


import json


class Student:
    """
    Student class section
    """

    def __init__(self, first_name, last_name, age):
        """class init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """
        JSON Representation of Sudent
        """

        return self.__dict__.copy()
