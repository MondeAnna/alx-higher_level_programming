#!/usr/bin/python3

for n in range(100):
    if n == 89:
        print("{}".format(n))
    elif n % 10 > n // 10 and n != 89:
        print("{}{}, ".format(n // 10, n % 10), end="")
