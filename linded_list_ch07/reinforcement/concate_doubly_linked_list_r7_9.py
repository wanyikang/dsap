# -*- coding: utf-8 -*-
from doubly_linked_list import DoublyLinkedList

class DLList(DoublyLinkedList):

    def concate(self, l):
        """ Concatenating self with l."""
        if type(self) != type(l):
            raise TypeError('Wrong type l')
        self_last = self._trailer._prev
        l_first = l._header._next
        self_last._next = l_first
        l_first._prev = self_last
        self._trailer = l._trailer
        self._size += l._size


if __name__ == '__main__':
    dllist = DLList()
    for i in range(11):
        dllist.add_first(i)
    dllist.traverse_print()

    dllist2 = DLList()
    for i in range(-1, -11, -1):
        dllist2.add_last(i)
    dllist2.traverse_print()

    dllist.concate(dllist2)
    dllist.traverse_print()
    print('len: {0:d}'.format(len(dllist)))

