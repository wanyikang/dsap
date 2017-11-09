# -*- coding: utf-8 -*-
from singly_linked_list import SinglyLinkedList
from exception import Empty

class LinkedList(SinglyLinkedList):
    """ LinkedList implementation based on SinglyLinkedList."""
    def second_to_last(self):
        if self._size < 2:
            raise Empty('Length of linked list is less than 2')
        prev = self._head
        walk = self._head
        while walk is not self._tail:
            prev = walk
            walk = walk._next
        return prev._element

if __name__ == '__main__':
    llist = LinkedList()
    for i in range(10):
        llist.add_first(i)
    print(llist.second_to_last())

