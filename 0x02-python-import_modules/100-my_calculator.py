#!/usr/bin/python3


from calculator_1 import add, sub, mul, div
import sys


def print_cli_args(args):
    arg_count = len(args)

    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>".format())
        exit(1)

    a, op, b = args

    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and / ".format())
        exit(1)

    func = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }[op]

    print("{} {} {} = {}".format(a, op, b, func(int(a), int(b))))


if __name__ == "__main__":
    args = sys.argv[1:]
    print_cli_args(args)
