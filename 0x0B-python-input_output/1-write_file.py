#!/usr/bin/python3


"""
Write to utf-8 encoded text file
"""


def write_file(filename="", text=""):
    """
    Write to utf-8 encoded text file
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
