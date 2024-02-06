#!/usr/bin/python3


"""
Append to utf-8 encoded text file
"""


def append_write(filename="", text=""):
    """
    Append to utf-8 encoded text file
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
