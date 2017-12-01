# -*- coding: utf-8 -*-
from _singly_linked_list import SinglyLinkedList
from exception import Empty

class LinkedQueue(SinglyLinkedList):
    """ A queue ADT based on singly linked list."""

    def enqueue(self, e):
        """ Add an element to the end of the queue."""
        self.add_last(e)

    def dequeue(self):
        """ Remove and return the first element of the queue. Raise Empty
        exception if it's empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.remove_first()

    def first(self):
        """ Return(but do not remove) first element of the queue. Raise Empty
        exception if it's empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.head()

if __name__ == "__main__":
    d = LinkedQueue()
    for i in range(10):
        d.enqueue(i)
        print(len(d))
    d.dequeue()
    print(d.first())
    print(d.is_empty())
    for i in range(9):
        d.dequeue()
    print(d.is_empty())

