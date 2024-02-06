#!/usr/bin/python3


"""
Pascal's Triangle
"""


def factorial(n):
    """
    Calculates factorial of n
    """

    if n <= 1:
        return 1
    return n * factorial(n - 1)


def combinations(n, k):
    """
    The number of ways, order unconcerned, we can
    items from a set
    """

    numerator = factorial(n)
    denominator = factorial(k) * factorial(n - k)
    return numerator / denominator


def pascal_row(n):
    """
    zero based calculation of row values of pascal's triable
    """

    return [int(combinations(n, k)) for k in range(n + 1)]


def pascal_triangle(n):
    """
    Pascal's Triangle, named after Blaise Pascal, a famous
    French Mathematician and Philosopher. To build the
    triangle, start with "1" at the top, then continue
    placing numbers below it in a triangular pattern. Each
    number is the numbers directly above it added together.
    """

    if n <= 0:
        return 0
    return [pascal_row(row) for row in range(n)]
