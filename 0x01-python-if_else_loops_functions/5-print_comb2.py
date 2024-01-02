#!/usr/bin/python3

for n in range(100):
    comma = "\n" if n == 99 else ", "
    if n <= 9:
        print("0{}{}".format(n, comma), end="")
    else:
        print("{}{}".format(n, comma), end="")
