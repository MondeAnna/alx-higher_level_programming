#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """ a function that divides element by element 2 lists """

    list_ = []

    for index in range(list_length):
        try:
            a = my_list_1[index]
            b = my_list_2[index]
            list_.append(a / b)
        except ZeroDivisionError:
            print("division by 0")
            list_.append(0)
        except TypeError:
            print("wrong type")
            list_.append(0)
        except IndexError:
            print("out of range")
            list_.append(0)
        finally:
            ...

    return list_
