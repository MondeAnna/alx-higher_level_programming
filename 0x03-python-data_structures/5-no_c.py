#!/usr/bin/python3


def no_c(my_string):
    idx = my_string.lower().find("c")

    if idx == -1:
        return my_string

    return no_c(my_string[:idx] + my_string[idx+1:])
