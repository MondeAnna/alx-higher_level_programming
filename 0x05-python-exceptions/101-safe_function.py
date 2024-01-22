#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """ a function that executes a function safely """
    try:
        return fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
