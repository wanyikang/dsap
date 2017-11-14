# -*- coding: utf-8 -*-
from singly_linked_list_with_sentinel import SinglyLinkedList
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

    def concatenate(self, q):
        """ Concatenate self and q. All the elements of q are append to self in
        the original order, and q will be set to empty after appending."""
        if self.is_empty():
            self._header._next = q._header._next
        else:
            self._tail._next = q._header._next
        if q._tail:
            self._tail = q._tail
        self._size += q._size
        # reset q
        q._header = self._Node(None, None)
        q._tail = None
        q._size = 0

if __name__ == "__main__":
    d = LinkedQueue()
    for i in range(10):
        d.enqueue(i)
        print(len(d))
    d.dequeue()
    print(d.first())
    print(d.is_empty())
    for i in range(2):
        d.dequeue()
    print(d.is_empty())

    q = LinkedQueue()
    d.concatenate(q)
    d.traverse_print()

    q = LinkedQueue()
    for i in range(10, 20):
        q.enqueue(i)
    d.concatenate(q)
    d.traverse_print()

    for i in range(17):
        d.dequeue()
    q = LinkedQueue()
    for i in range(10, 20):
        q.enqueue(i)
    d.concatenate(q)
    d.traverse_print()

    print('q: ')
    q.traverse_print()

