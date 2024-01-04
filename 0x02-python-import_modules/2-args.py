#!/usr/bin/python3


import sys


def print_cli_args(args):
    arg_count = len(args)

    descriptor = "argument" if arg_count == 1 else "arguments"
    closing = "." if not arg_count else ":"

    print("{} {}{}".format(arg_count, descriptor, closing))

    if not arg_count:
        return

    for index, arg in enumerate(args, start=1):
        print("{}: {}".format(index, arg))


if __name__ == "__main__":
    args = sys.argv[1:]
    print_cli_args(args)
