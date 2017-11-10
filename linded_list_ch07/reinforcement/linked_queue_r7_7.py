# -*- coding: utf-8 -*-
from singly_linked_list import SinglyLinkedList
from exception import Empty

class LinkedQueue(SinglyLinkedList):
    """ An implementation of queue based on singly linked list."""

    def first(self):
        """ Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.head()

    def dequeue(self):
        """ Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.remove_first()

    def enqueue(self, e):
        """ Add an element to the back of queue."""
        self.add_last(e)

    def rotate(self):
        """ Rotate the queue left one element."""
        if self._size > 1:
            old_head = self._head
            self._head = self._head._next
            self._tail._next = old_head
            old_head._next = None
            self._tail = old_head

if __name__ == '__main__':
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(i)
    q.traverse_print()
    q.rotate()
    q.traverse_print()

