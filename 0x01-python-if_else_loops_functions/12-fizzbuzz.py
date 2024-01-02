#!/usr/bin/python3


def fizzbuzz():
    for n in range(1, 101):
        if not n % 3 and not n % 5:
            print("{}".format("FizzBuzz"), end=" ")
        elif not n % 3:
            print("{}".format("Fizz"), end=" ")
        elif not n % 5:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(n), end=" ")
