#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    zeroes = 0, 0

    tuple_a = (*tuple_a, *zeroes)[:2]
    tuple_b = (*tuple_b, *zeroes)[:2]

    return tuple(
        sum(iterable_)
        for iterable_ in zip(tuple_a, tuple_b)
    )
