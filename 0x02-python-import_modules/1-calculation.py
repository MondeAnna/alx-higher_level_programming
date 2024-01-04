#!/usr/bin/python3


from calculator_1 import add, sub, mul, div


a = 10
b = 5


if __name__ == "__main__":
    for op, func in zip("+-*/", (add, sub, mul, div)):
        print("{} {} {} = {}".format(a, op, b, func(a, b)))
