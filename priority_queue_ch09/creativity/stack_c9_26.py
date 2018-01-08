# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from priqueues.heap_priority_queue import HeapPriorityQueue
from priqueues.collections.exception import Empty

class Stack(object):
    """ A stack implementation base on heap priority queue."""

    def __init__(self):
        """ Create an empty stack."""
        self._key = 0  # keep the key minimum
        self._pq = HeapPriorityQueue()

    def __len__(self):
        """ Return the number of elements in the stack."""
        return len(self._pq)

    def is_empty(self):
        """ Return True if the stack is empty."""
        return len(self) == 0

    def push(self, e):
        """ Add element e to the top of the stack."""
        self._pq.add(self._key, e)
        self._key -= 1

    def pop(self):
        """ Remove and return the element from the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        key, value = self._pq.remove_min()
        return value

    def top(self):
        """ Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        key, value = self._pq.min()
        return value

if __name__ == "__main__":
    s = Stack()
    for i in range(20):
        s.push(i)
    print('top: {0}, len: {1}'.format(s.top(), len(s)))
    s.pop()
    print('top: {0}, len: {1}'.format(s.top(), len(s)))
    s.pop()
    print('top: {0}, len: {1}'.format(s.top(), len(s)))

