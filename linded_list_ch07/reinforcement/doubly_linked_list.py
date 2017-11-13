# -*- coding: utf-8 -*-
from exception import Empty

class DoublyLinkedList(object):
    """ A doubly linked list implementation."""

    class _Node(object):
        """ Node class for doubly linked list."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, nxt):
            self._element = element
            self._prev = prev
            self._next = nxt

    def __init__(self):
        self._header = self._Node(None, None, None)  # head sentinel
        self._trailer = self._Node(None, self._header, None)  # tail sentinel
        self._header._next = self._trailer
        self._size = 0

    def __len__(self):
        """ Return the length of the doubly linked list."""
        return self._size

    def is_empty(self):
        """ Return True if the doubly linked list is empty."""
        return self._size == 0

    def first(self):
        """ Return element of the first node in doubly linked list. Raise Empty
        exception if it's empty."""
        if self.is_empty():
            raise Empty('Doubly linked list is empty')
        return self._header._next._element

    def last(self):
        """ Return element of the last node in doubly linked list. Raise Empty
        exception if it's empty."""
        if self.is_empty():
            raise Empty('Doubly linked list is empty')
        return self._trailer._prev._element

    def add_first(self, e):
        """ Add element to first of the doubly linked list."""
        self._add_between(e, self._header, self._header._next)

    def add_last(self, e):
        """ Add element to last of the doubly linked list."""
        self._add_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """ Delete first node, and Return the element. Raise Empty exception if
        the list is empty."""
        if self._size == 0:
            raise Empty('the doubly linked list is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        """ Delete last node, and Return the element. Raise Empty exception if
        the list is empty."""
        if self._size == 0:
            raise Empty('the doubly linked list is empty')
        return self._delete_node(self._trailer._prev)

    def _insert_between(self, e, predecessor, successor):
        return self._add_between(e, predecessor, successor)

    def _add_between(self, e, predecessor, successor):
        """ Add an element between predecessor and successor. Return the new
        created node."""
        node = self._Node(e, predecessor, successor)
        predecessor._next = node
        successor._prev = node
        self._size += 1
        return node

    def _delete_node(self, node):
        """ Delete the node specified by `node`, and Return the element of
        `node`."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def traverse_print(self):
        """ Traverse the doubly linked list and print all the elements."""
        walk = self._header._next
        while walk is not None:
            if walk is self._trailer:
                break
            print('{0:d}'.format(walk._element))
            walk = walk._next
        print('\n')

if __name__ == '__main__':
    dllist = DoublyLinkedList()
    for i in range(10):
        dllist.add_first(i)
    dllist.traverse_print()

    for i in range(-1, -11, -1):
        dllist.add_last(i)
    dllist.traverse_print()
    print('first: {0:d}, last: {1:d}, len: {2:d}'.format(dllist.first(),
        dllist.last(), len(dllist)))

    for i in range(8):
        dllist.delete_first()
    for i in range(8):
        dllist.delete_last()
    dllist.traverse_print()
    print('first: {0:d}, last: {1:d}, len: {2:d}'.format(dllist.first(),
        dllist.last(), len(dllist)))

