# -*- coding: utf-8 -*-
from exception import Empty

class DoublyLinkedList(object):
    """ A doubly linked list implementation without sentinels."""

    class _Node(object):
        """ Node class for doubly linked list."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, nxt):
            self._element = element
            self._prev = prev
            self._next = nxt

    def __init__(self):
        self._head = None  # _head means the really first node, not sentinel
        self._tail = None  # _tail means the really last node, not sentinel
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
        return self._head._element

    def last(self):
        """ Return element of the last node in doubly linked list. Raise Empty
        exception if it's empty."""
        if self.is_empty():
            raise Empty('Doubly linked list is empty')
        return self._tail._element

    def add_first(self, e):
        """ Add element to first of the doubly linked list."""
        self._insert_between(e, None, self._head)

    def add_last(self, e):
        """ Add element to last of the doubly linked list."""
        self._insert_between(e, self._tail, None)

    def delete_first(self):
        """ Delete first node, and Return the element. Raise Empty exception if
        the list is empty."""
        if self._size == 0:
            raise Empty('the doubly linked list is empty')
        return self._delete_node(self._head)

    def delete_last(self):
        """ Delete last node, and Return the element. Raise Empty exception if
        the list is empty."""
        if self._size == 0:
            raise Empty('the doubly linked list is empty')
        return self._delete_node(self._tail)

    def _insert_between(self, e, predecessor, successor):
        """ Insert an element between predecessor and successor. Return the new
        created node."""
        newnode = self._Node(e, predecessor, successor)
        if predecessor is not None:
            predecessor._next = newnode
        else:
            self._head = newnode
        if successor is not None:
            successor._prev = newnode
        else:
            self._tail = newnode
        self._size += 1
        return newnode

    def _delete_node(self, node):
        """ Delete the node specified by `node`, and Return the element of
        `node`."""
        predecessor = node._prev
        successor = node._next
        if predecessor:
            predecessor._next = successor
        else:
            self._head = node._next
        if successor:
            successor._prev = predecessor
        else:
            self._tail = node._prev
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def __repr__(self):
        """ String representation of the doubly linked list."""
        s = ''
        walk = self._head
        while walk is not None:
            s += str(walk._element) + ','
            walk = walk._next
        return s[:-1]

if __name__ == '__main__':
    dllist = DoublyLinkedList()
    for i in range(10):
        dllist.add_first(i)
    print('for i in range(10): add_first(i)')
    print(dllist)
    print('first: {0:d}, last: {1:d}, len: {2:d}'.format(dllist.first(),
        dllist.last(), len(dllist)))
    print('')

    for i in range(-1, -11, -1):
        dllist.add_last(i)
    print('for i in range(-1, -11, -1): add_last(i)')
    print(dllist)
    print('first: {0:d}, last: {1:d}, len: {2:d}'.format(dllist.first(),
        dllist.last(), len(dllist)))
    print('')

    for i in range(8):
        dllist.delete_first()
    print('for i in range(8): delete_first()')
    print(dllist)
    print('first: {0:d}, last: {1:d}, len: {2:d}'.format(dllist.first(),
        dllist.last(), len(dllist)))
    print('')

    for i in range(8):
        dllist.delete_last()
    print('for i in range(8): delete_last()')
    print(dllist)
    print('first: {0:d}, last: {1:d}, len: {2:d}'.format(dllist.first(),
        dllist.last(), len(dllist)))
    print('')

