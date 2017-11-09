# -*- coding: utf-8 -*-
from exception import Empty

class SinglyLinkedList(object):
    """ ADT of singly linked list."""

    class _Node(object):
        """ Node class for SinglyLinkedList."""
        __slot__ = '_element', '_next'  # streamline the memory management
        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def add_first(self, e):
        """ Add an element to the first of the linked list."""
        self._head = self._Node(e, self._head)
        if self._size == 0:
            self._tail = self._head
        self._size += 1

    def remove_first(self):
        """ Remove the first element to the linked list and return the first
        element."""
        if self._size == 0:
            raise Empty('Singly linked list is empty!')
        tmp = self._head
        rlt = tmp._element
        self._head = self._head._next
        tmp._next = tmp._element = None
        if self._size == 1:
            self._tail = self._head
        self._size -= 1
        return rlt

    def add_last(self, e):
        """ Add an element to the last of the linked list."""
        tmp = self._Node(e, None)
        if self._size == 0:
            self._tail = self._head = tmp
        else:
            self._tail._next = tmp
            self._tail = tmp
        self._size += 1

    def traverse_print(self):
        """ Traverse the linked list and print all the elements."""
        walk = self._head
        while walk is not None:
            print('{0:d}'.format(walk._element))
            walk = walk._next
        print('\n')

if __name__ == '__main__':
    sllist = SinglyLinkedList()
    for i in range(10):
        sllist.add_first(i)
    sllist.traverse_print()

    for i in range(-1, -11, -1):
        sllist.add_last(i)
    sllist.traverse_print()

    for i in range(15):
        sllist.remove_first()
    sllist.traverse_print()

