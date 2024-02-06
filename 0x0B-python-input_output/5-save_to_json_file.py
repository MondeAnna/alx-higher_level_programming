#!/usr/bin/python3


"""
Write JSON Representation to File
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write JSON Representation to File
    """

    with open(filename, "w", encoding="utf-8") as file:
        json_obj = json.dumps(my_obj)
        return file.write(json_obj)
