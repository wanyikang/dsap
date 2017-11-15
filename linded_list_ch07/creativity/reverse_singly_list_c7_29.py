# -*- coding: utf-8 -*-
from singly_linked_list import SinglyLinkedList

class SList(SinglyLinkedList):

    def _recursive_reverse(self, walk):
        """ Reverse the singly linked list by recursiving."""
        if walk._next is None:
            return (walk, walk)
        else:
            (head, tail) = self._recursive_reverse(walk._next)
            tail._next = walk
            walk._next = None
            return (head, walk)

    def recursive_reverse(self):
        """ Reverse the singly linked list by recursiving."""
        if self.is_empty():
            return
        (head, tail) = self._recursive_reverse(self._head)
        self._head = head
        self._tail = tail

    def iterate_reverse(self):
        """ Reverse the singly linked list by iterating."""
        if self._size <= 1:
            return
        head = self._head
        pre_walk = self._head._next
        walk = pre_walk._next
        head._next = None
        while walk is not None:
            pre_walk._next = head
            head = pre_walk
            pre_walk = walk
            walk = walk._next
        pre_walk._next = head
        head = pre_walk
        self._tail = self._head
        self._head = head

if __name__ == '__main__':
    l = SList()
    for i in range(20):
        l.add_last(i)
    print('original: {0:s}'.format(str(l)))
    l.recursive_reverse()
    print('recursive: {0:s}'.format(str(l)))
    l.iterate_reverse()
    print('iterate: {0:s}'.format(str(l)))

