# -*- coding: utf-8 -*-
from singly_linked_list import SinglyLinkedList

class LinkedList(SinglyLinkedList):

    def swap(self, x, y):
        """ Swap the elements in the linked list, the target elements are
        referenced by x and y. Assume the x and y are in this singly linked
        list.
        """
        bx = self._before(x)
        by = self._before(y)
        nx = x._next
        ny = y._next

        # swap x and y
        if bx:
            bx._next = y
        if nx is not y:
            y._next = nx
        else:
            y._next = x  # x is immediately precede y
        if by:
            by._next = x
        if ny is not x:
            x._next = ny  # y is immediately precede x
        else:
            x._next = y

        # adjust head
        if x is self._head:
            self._head = y
            return
        if y is self._head:
            self._head = x

if __name__ == '__main__':
    llist = LinkedList()
    for i in range(10):
        llist.add_first(i)
    llist.traverse_print()

    x = llist._head
    y = llist._head
    for i in range(9):
        y = y._next
    llist.swap(x, y)
    llist.traverse_print()
    llist.swap(x, y)
    llist.traverse_print()

    x = y = llist._head
    llist.swap(x, y)
    llist.traverse_print()

    x = llist._head
    y = x._next
    llist.swap(x, y)
    llist.traverse_print()

    x = llist._head._next
    y = x._next
    llist.swap(x, y)
    llist.traverse_print()

    x = llist._head
    for i in range(8):
        x = x._next
    y = llist._head
    for i in range(9):
        y = y._next
    llist.swap(x, y)
    llist.traverse_print()

