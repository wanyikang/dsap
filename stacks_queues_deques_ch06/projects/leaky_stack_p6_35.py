# -*- coding: utf-8 -*-

class LeakyStack(object):
    """ Implementation of a leaky stack.
    When push is invoked with the stack at full capacity, accept the pushed
    element at the top while “leaking” the oldest element from the bottom of
    the stack to make room.
    """
    DEFAULT_CAPACITY = 10

    def __init__(self, maxlen):
        super(LeakyStack, self).__init__()
        self._maxlen = maxlen
        self._data = [None] * LeakyStack.DEFAULT_CAPACITY
        self._front = 0
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack.
        When stack is full, drop the bottom element to make room for new
        element.
        """
        # if reach the maxlen size
        if self._size == self._maxlen:
            self._front = (self._front + 1) % len(self._data)
            avail = (self._front + self._size - 1) % len(self._data)
            self._data[avail] = e
            return
        # not reach the maxlen size
        if self._size == len(self._data):
            self._resize(2 * self._size)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def pop(self):
        """Remove and return the element from the top of the stack (i.e.,
        LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty!')
        last = (self._front + self._size - 1) % len(self._data)
        rlt = self._data[last]
        self._data[last] = None  # help gc
        self._size -= 1
        # resize the underlying list
        if self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return rlt

    def top(self):
        """ Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty!')
        last = (self._front + self._size - 1) % len(self._data)
        return self._data[last]

    def _resize(self, cap):
        """ Resize the underlying list to length `cap`."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

if __name__ == '__main__':
    s = LeakyStack(20)
    for i in range(20):
        s.push(i)
    print(s._data)
    print('front: {0}, size: {1}'.format(s._front, s._size))
    s.push(20)
    print(s._data)
    print('front: {0}, size: {1}'.format(s._front, s._size))
    for i in range(19):
        s.pop()
    print(s._data)
    print('front: {0}, size: {1}'.format(s._front, s._size))

