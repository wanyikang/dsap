# -*- coding: utf-8 -*-
from doubly_linked_list import DoublyLinkedList

class DLList(DoublyLinkedList):

    def middle(self):
        """ Return the middle element of the doubly linked list. If the size of
        the list is even, Return the slightly left element. Return None if the
        list is empty.
        Note: we only can use link hopping, no counter.
        """
        if self.is_empty():
            return None
        first = self._header._next
        last = self._trailer._prev
        while True:
            if first is last:
                break
            elif first._next is last and last._prev is first:
                break
            else:
                first = first._next
                last = last._prev
        return first._element

if __name__ == '__main__':
    dllist = DLList()
    for i in range(11):
        dllist.add_first(i)
    dllist.traverse_print()
    middle = dllist.middle()
    if middle:
        print('middle element: {0:d}'.format(middle))

