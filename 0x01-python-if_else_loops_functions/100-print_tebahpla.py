#!/usr/bin/python3


def to_upper(c):
    to_subtract = ord("a") - ord("A")
    diff = ord(c) - to_subtract
    return chr(diff)


def is_odd(i):
    return i % 2


for i, c in enumerate(reversed("abcdefghijklmnopqrstuvwxyz")):
    print("{}".format(to_upper(c) if is_odd(i) else c), end="")
