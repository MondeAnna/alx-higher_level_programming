#!/usr/bin/python3


""" Base class """


import json
import csv
import os


class Base:

    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ where id is none, set id to current object count """

        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @classmethod
    def create(cls, **dictionary):
        """ create a new object with provided dictionary (a.k.a. kwargs)"""

        obj = cls(**dictionary)
        obj.update(**dictionary)
        return obj

    @staticmethod
    def from_json_string(json_string):
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """ load json file into list of objects """

        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as file:
            entries = Base.from_json_string(file.read())
            return [cls.create(**entry) for entry in entries]

    @classmethod
    def load_from_file_csv(cls):
        """ load csv file into list of objects """

        filename = f"{cls.__name__}.csv"

        if not os.path.exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            entries = [
                {
                    key: int(value) if value.isdigit else value
                    for key, value in entry.items()
                }
                for entry in reader
            ]
            return [cls.create(**entry) for entry in entries]

    @classmethod
    def save_to_file(cls, list_objs):
        filename = Base.__get_filename(list_objs, "json")

        dict_objs = [
            obj.to_dictionary() for obj in list_objs
        ] if list_objs else []
        str_objs = Base.to_json_string(dict_objs)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(str_objs)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = Base.__get_filename(list_objs, "csv")
        fields = Base.__get_fields(list_objs)

        dict_objs = [
            obj.to_dictionary() for obj in list_objs
        ] if list_objs else []

        with open(filename, "w", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(dict_objs)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ provide json string of object """

        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def __get_fields(list_objs):
        if not list_objs:
            return []

        obj = list_objs[0]

        return {
            "rectangle": ["id", "width", "height", "x", "y"],
            "square": ["id", "size", "x", "y"],
        }.get(obj.__class__.__name__.lower(), [])

    @staticmethod
    def __get_filename(list_objs, file_type):
        if not list_objs:
            return f"Base.{file_type}"
        else:
            obj_01 = list_objs[0]
            filename = obj_01.__class__.__name__
            return f"{filename}.{file_type}"

    def __del__(self):
        """ decrement object count upon destruction """

        Base.__nb_objects -= 1
