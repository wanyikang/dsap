# -*- coding: utf-8 -*-
from circularly_linked_list import CircularlyLinkedList

class CLList(CircularlyLinkedList):

    def count_by_loop(self):
        if self._tail is None:
            return 0
        elif self._tail is self._tail._next:
            return 1
        else:
            rlt = 1
            walk = self._tail._next
            while walk is not self._tail:
                rlt += 1
                walk = walk._next
            return rlt

if __name__ == '__main__':
    cllist = CLList()
    for i in range(999):
        cllist.add_first(i)
    print('count: {0:d}'.format(cllist.count_by_loop()))

