#!/usr/bin/python3

""" Define node of a singly linked list """


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstace(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if not self.__head:
            self.__head = value
            return

        curr = self.__head

        while value.data > self.__head.data:
            curr = self.__head
            self.__head = self.__head.next_node

        curr.next_node = value
        value.next_node = self.__head

    def __str__(self):
        data = []
        node = self.__head

        while node:
            data.append(node.data)
            node = node.next_node

        return "\n".join(str(datum) for datum in data)
