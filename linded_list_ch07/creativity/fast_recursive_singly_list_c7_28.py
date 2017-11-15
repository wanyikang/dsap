# -*- coding: utf-8 -*-
from singly_linked_list import SinglyLinkedList

class SList(SinglyLinkedList):

    def _reverse(self, walk):
        """ Reverse the singly linked list by recursiving."""
        if walk._next is None:
            return (walk, walk)
        else:
            (head, tail) = self._reverse(walk._next)
            tail._next = walk
            walk._next = None
            return (head, walk)

    def reverse(self):
        """ Reverse the singly linked list by recursiving."""
        if self.is_empty():
            return
        (head, tail) = self._reverse(self._head)
        self._head = head
        self._tail = tail

if __name__ == '__main__':
    l = SList()
    for i in range(20):
        l.add_last(i)
    print('original: {0:s}'.format(str(l)))
    l.reverse()
    print('reversed: {0:s}'.format(str(l)))

