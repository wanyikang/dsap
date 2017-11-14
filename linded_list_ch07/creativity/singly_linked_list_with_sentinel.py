# -*- coding: utf-8 -*-
from exception import Empty

class SinglyLinkedList(object):
    """ ADT of singly linked list that has a sentinel in the inner
    implemetation."""

    class _Node(object):
        """ Node class for SinglyLinkedList."""
        __slot__ = '_element', '_next'  # streamline the memory management
        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._tail = None
        self._header = self._Node(None, None)
        self._size = 0

    def __len__(self):
        """ Return the length of the singly linked list."""
        return self._size

    def is_empty(self):
        """ Return Ture if the list is empty."""
        return self._size == 0

    def head(self):
        """ Return the head element of the singly linked list. If the list is
        empty then return None.
        """
        return self._header._next._element

    def tail(self):
        """ Return the tail element of the singly linked list. If the list is
        empty then return None.
        """
        return self._tail._element

    def add_first(self, e):
        """ Add an element to the first of the linked list."""
        newnode = self._Node(e, self._header._next)
        self._header._next = newnode
        if self._size == 0:
            self._tail = newnode
        self._size += 1

    def remove_first(self):
        """ Remove the first element to the linked list and return the first
        element."""
        if self._size == 0:
            raise Empty('singly list is Empty')
        node = self._header._next
        rlt = node._element
        self._header._next = node._next
        node._element = node._next = None
        self._size -= 1
        if self._size == 0:
            self._tail = None
        return rlt

    def add_last(self, e):
        """ Add an element to the last of the linked list."""
        newnode = self._Node(e, None)
        if self._size == 0:
            self._header._next = newnode
        else:
            self._tail._next = newnode
        self._tail = newnode
        self._size += 1

    def traverse_print(self):
        """ Traverse the linked list and print all the elements."""
        walk = self._header._next
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
    print('head: {0:d}, tail: {1:d}'.format(sllist.head(), sllist.tail()))
    sllist.traverse_print()

    walk = sllist._header._next
    for i in range(4):
        walk = walk._next

    print(walk._element)

