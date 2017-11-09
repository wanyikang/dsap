# -*- coding: utf-8 -*-
from singly_linked_list import SinglyLinkedList

class LinkedList(SinglyLinkedList):

    def recursive_count(self):
        if self._head is None:
            return 0
        else:
            self.remove_first()
            return self.recursive_count() + 1

if __name__ == '__main__':
    llist = LinkedList()
    for i in range(100):
        llist.add_first(i)
    print(llist.recursive_count())

