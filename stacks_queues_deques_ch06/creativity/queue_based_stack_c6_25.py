# -*- coding: utf-8 -*-
from array_stack_c6_16 import ArrayStack
from exception import Empty

class Queue(object):
    """ Queue impelemented based on stack."""
    def __init__(self):
        self._stack = ArrayStack()
        self._rstack = ArrayStack()
        self._len = 0
        self._first = None

    def enqueue(self, e):
        """ Add an element to the end of the queue."""
        self._stack.push(e)
        if self._len == 0:
            self._first = e
        self._len += 1

    def dequeue(self):
        """ Remove the first element of the queue.
        if the _rstack is not empty, then directly pop one from the _rstack. if
        empty, _copy_to_stack first and then pop one from _rstack.
        """
        if self._len == 0:
            raise Empty('Queue is empty!')
        elif len(self._rstack) == 0:
            self._copy_to_rstack()
        self._len -= 1
        first = self._rstack.pop()
        # update first
        if len(self._rstack) == 0:
            self._copy_to_rstack()
        if self._len > 0:
            self._first = self._rstack.top()
        else:
            self._first = None
        return first

    def first(self):
        """ Get the first element of the queue."""
        if self._len == 0:
            raise Empty('Queue is empty!')
        else:
            return self._first

    def _copy_to_rstack(self):
        """ Pop elements from _stack and push them to _rstack one by one."""
        for i in range(self._len):
            e = self._stack.pop()
            self._rstack.push(e)

    def __len__(self):
        return self._len

    def is_empty(self):
        """ Check if the queue is empty or not."""
        return self._len == 0

if __name__ == "__main__":
    d = Queue()
    for i in range(10):
        d.enqueue(i)
    d.dequeue()
    print('first: {0:d}'.format(d.first()))
    for i in range(10, 20):
        d.enqueue(i)
    for i in range(19):
        print('first: {0:d}'.format(d.first()))
        d.dequeue()
    print('queue is empty: {0:s}'.format(str(d.is_empty())))

