# -*- coding: utf-8 -*-
from singly_linked_list import SinglyLinkedList

class LinkedList(SinglyLinkedList):

    def concate(self, ll):
        """ Concatenating self and linked list ll only by using the head
        elements of them. Elements of self come first.
        """
        if type(self) != type(ll):
            raise TypeError('Wrong type of ll')
        walk = self._head
        while walk._next is not None:
            walk = walk._next
        walk._next = ll._head

if __name__ == '__main__':
    llone = LinkedList()
    for i in range(10):
        llone.add_first(i)
    llone.traverse_print()

    lltwo = LinkedList()
    for i in range(10, 20):
        lltwo.add_first(i)
    lltwo.traverse_print()

    llone.concate(lltwo)
    llone.traverse_print()

