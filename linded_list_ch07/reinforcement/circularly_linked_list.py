# -*- coding: utf-8 -*-
from exception import Empty

class CircularlyLinkedList(object):
    """ An implementation of circular linked list."""

    class _Node(object):
        """ Node class for circular linked list."""
        __slots__ = '_element', '_next'

        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        super(CircularlyLinkedList, self).__init__()
        self._tail = None
        self._size = 0

    def __len__(self):
        """ Return the length of the list."""
        return self._size

    def first(self):
        """ Return the first element in the circularly linked list. Raise Empty
        exception if the list is empty."""
        if self._size == 0:
            raise Empty('Circularly linked list is empty')
        return self._tail._next._element

    def last(self):
        """ Return the last element in the circularly linked list. Raise Empty
        exception if the list is empty."""
        if self._size == 0:
            raise Empty('Circularly linked list is empty')
        return self._tail._element

    def add_first(self, e):
        """ Add the element `e` to the first of the list."""
        if self._size == 0:
            self._tail = self._Node(e, None)
            self._tail._next = self._tail
            self._size += 1
        else:
            first = self._tail._next
            newnode = self._Node(e, first)
            self._tail._next = newnode
            self._size += 1

    def remove_first(self):
        """ Remove and return the first element in the list. Raise Empty
        exception if the list is empty."""
        if self._size == 0:
            raise Empty('Circularly linked list is empty')
        first = self._tail._next
        self._tail._next = first._next
        rlt = first._element
        first._element = first._next = None
        self._size -= 1
        if self._size == 0:
            self._tail = None  # edge condition
        return rlt

    def add_last(self, e):
        """ Add the element `e` to the last of the list."""
        if self._size == 0:
            self._tail = self._Node(e, None)
            self._tail._next = self._tail
            self._size += 1
        else:
            first = self._tail._next
            newnode = self._Node(e, first)
            self._tail._next = newnode
            self._tail = newnode
            self._size += 1

    def traverse_print(self):
        """ Traverse the linked list and print all the elements."""
        if self._size == 0:
            return
        if self._size == 1:
            print('{0:d}'.format(self._tail._element))
            return
        walk = self._tail._next
        while walk is not self._tail:
            print('{0:d}'.format(walk._element))
            walk = walk._next
        print('{0:d}'.format(self._tail._element))

if __name__ == '__main__':
    cllist = CircularlyLinkedList()
    for i in range(10):
        cllist.add_first(i)
    for i in range(-1, -10, -1):
        cllist.add_last(i)
    cllist.traverse_print()
    print('first: {0:d}, last: {1:d}, len: {2:d}\n'.format(cllist.first(),
        cllist.last(), len(cllist)))

    for i in range(15):
        cllist.remove_first()
    cllist.traverse_print()
    print('first: {0:d}, last:{1:d}, len: {2:d}\n'.format(cllist.first(),
        cllist.last(), len(cllist)))

