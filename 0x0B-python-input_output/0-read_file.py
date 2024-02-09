#!/usr/bin/python3


"""
Read utf-8 encoded text file
"""


def read_file(filename=""):
    """
    Read utf-8 encoded text file
    """

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
