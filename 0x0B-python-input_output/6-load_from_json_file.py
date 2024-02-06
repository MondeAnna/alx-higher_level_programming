#!/usr/bin/python3


"""
Create Object from JSON File
"""


import json


def load_from_json_file(filename):
    """
    Create Object from JSON File
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
