#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = sum(a * b for a, b in my_list)
    denominator = sum(total for _, total in my_list)

    return numerator / denominator
