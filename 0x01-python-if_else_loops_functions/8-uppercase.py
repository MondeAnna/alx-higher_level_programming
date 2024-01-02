#!/usr/bin/python3


def uppercase(str):
    for c in str:
        print("{}".format(to_upper(c) if islower(c) else c), end="")
    print()


def to_upper(c):
    to_subtract = ord("a") - ord("A")
    diff = ord(c) - to_subtract
    return chr(diff)


def islower(c):
    return ord("a") <= ord(c) <= ord("z")
