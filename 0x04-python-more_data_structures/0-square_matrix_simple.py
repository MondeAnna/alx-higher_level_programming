#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    return [[x*x for x in row] for row in matrix]
