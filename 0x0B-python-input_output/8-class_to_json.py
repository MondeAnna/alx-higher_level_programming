#!/usr/bin/python3


"""
JSON Representation of Class
"""


import json


def class_to_json(obj):
    """
    JSON Representation of Class
    """

    return obj.__dict__.copy() if hasattr(obj, "__dict__") else {}
