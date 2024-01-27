#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """ a function that prints x elements of a list """
    num_printed = 0
    try:
        for enumeration, index in enumerate(range(x), start=1):
            print(my_list[index], end="")
            num_printed = enumeration
    except IndexError as error:
        ...
    finally:
        print()
    return num_printed
