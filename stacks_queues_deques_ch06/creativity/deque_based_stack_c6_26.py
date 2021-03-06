# -*- coding: utf-8 -*-
from array_stack_c6_16 import ArrayStack
from exception import Empty

class Deque(object):
    """ Deque impelemented based on stack.
    Asyptotic complexity:
    add_first: O(1)
    add_last: O(1)
    delete_first: O(1) amortized
    delete_last: O(1) amortized
    first: O(1)
    last: O(1)
    len: O(1)
    is_empty:O(1)
    """
    def __init__(self):
        self._lstack = ArrayStack()
        self._rstack = ArrayStack()
        self._len = 0
        self._first = None
        self._last = None

    def add_first(self, e):
        self._lstack.push(e)
        self._len += 1
        self._first = e

    def add_last(self, e):
        self._rstack.push(e)
        self._len += 1
        self._last = e

    def delete_first(self):
        if self._len == 0:
            raise Empty('Deque is empty!')
        elif len(self._lstack) == 0:
            self._copy_stack(self._rstack, self._lstack)
        first = self._lstack.pop()
        self._len -= 1
        # update first
        if len(self._lstack) == 0:
            self._copy_stack(self._rstack, self._lstack)
        if self._len > 0:
            self._first = self._lstack.top()
        return first

    def delete_last(self):
        if self._len == 0:
            raise Empty('Deque is empty!')
        elif len(self._rstack) == 0:
            self._copy_stack(self._lstack, self._rstack)
        last = self._rstack.pop()
        self._len -= 1
        # update last
        if len(self._rstack) == 0:
            self._copy_stack(self._lstack, self._rstack)
        if self._len > 0:
            self._last = self._rstack.top()
        return last

    def first(self):
        if self._len == 0:
            raise Empty('Deque is empty!')
        else:
            return self._first

    def last(self):
        if self._len == 0:
            raise Empty('Deque is empty!')
        else:
            return self._last

    def _copy_stack(self, src, dst):
        for i in range(len(src)):
            e = src.pop()
            dst.push(e)

    def __len__(self):
        return self._len

    def is_empty(self):
        """ Check if the queue is empty or not."""
        return self._len == 0

if __name__ == "__main__":
    d = Deque()
    for i in range(10):
        d.add_first(i)
    for i in range(10, 20):
        d.add_last(i)
    print('first: ', d.first())
    print('last: ', d.last())
    print('is_empty: {0}, len: {1:d}'.format(str(d.is_empty()), len(d)))
    for i in range(15):
        d.delete_first()
    print('first: ', d.first())
    print('last: ', d.last())
    print('is_empty: {0}, len: {1:d}'.format(str(d.is_empty()), len(d)))
    for i in range(3):
        d.delete_last()
    print('first: ', d.first())
    print('last: ', d.last())
    print('is_empty: {0}, len: {1:d}'.format(str(d.is_empty()), len(d)))

