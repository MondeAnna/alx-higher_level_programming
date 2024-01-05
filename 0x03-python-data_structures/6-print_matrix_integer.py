#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in row:
            closure = "\n" if elem == row[-1] else ", "
            print("{}{}".format(elem, closure), end="")
