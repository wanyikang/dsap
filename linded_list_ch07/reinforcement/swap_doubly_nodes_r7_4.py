# -*- coding: utf-8 -*-
from doubly_linked_list import DoublyLinkedList

class DLList(DoublyLinkedList):

    def swap(self, x, y):
        """ Swap node x and y. Assume x and y are nodes in this doubly linked
        list."""
        xp = x._prev
        xn = x._next
        yp = y._prev
        yn = y._next

        # y replace x
        if xp is not y:
            xp._next = y
        else:
            xp._next = xn
        if xp is not y:
            y._prev = xp
        else:
            y._prev = x
        if xn is not y:
            xn._prev = y
        else:
            xn._prev = xp
        if xn is not y:
            y._next = xn
        else:
            y._next = x

        # x replace y
        if yp is not x:
            yp._next = x
        else:
            yp._next = yn
        if yp is not x:
            x._prev = yp
        else:
            x._prev = y
        if yn is not x:
            yn._prev = x
        else:
            yn._prev = yp
        if yn is not x:
            x._next = yn
        else:
            x._next = y

if __name__ == '__main__':
    dllist = DLList()
    for i in range(10):
        dllist.add_first(i)
    dllist.traverse_print()

    x = dllist._header._next
    y = x._next._next
    dllist.swap(x, y)
    dllist.traverse_print()

    x = dllist._header._next
    y = x._next
    dllist.swap(x, y)
    dllist.traverse_print()

    x = dllist._header._next._next
    y = x._next._next
    dllist.swap(x, y)
    dllist.traverse_print()

