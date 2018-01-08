# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from priqueues.heap_priority_queue import HeapPriorityQueue
from priqueues.collections.exception import Empty

class Queue(object):
    """ A queue implementation using a heap priority queue."""

    def __init__(self):
        """ Create an empty queue."""
        self._key = 0  # keep the key maximum
        self._pq = HeapPriorityQueue()

    def __len__(self):
        """ Return the number of elements in the queue."""
        return len(self._pq)

    def is_empty(self):
        """ Return True if the queue is empty."""
        return len(self) == 0

    def enqueue(self, e):
        """ Add an element to the back of queue."""
        self._pq.add(self._key, e)
        self._key += 1

    def dequeue(self):
        """ Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        key, value = self._pq.remove_min()
        return value

    def first(self):
        """ Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        key, value = self._pq.min()
        return value

if __name__ == '__main__':
    d = Queue()
    for i in range(10):
        d.enqueue(i)
        print(len(d))
    d.dequeue()
    print(d.first())
    print(d.is_empty())
    for i in range(9):
        d.dequeue()
    print(d.is_empty())

