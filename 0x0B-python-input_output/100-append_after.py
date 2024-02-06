#!/usr/bin/python3


"""
Insert Line Into Text
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert Line Into Text
    """
    string = ""

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

        for line in lines:
            string += line

            if search_string in line:
                string += new_string

    with open(filename, "w", encoding="utf-8") as file:
        file.write(string)
