# -*- coding: utf-8 -*-
from exception import Empty

class ArrayDeque(object):
    """ Deque implementation ueing a python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """ Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """ Return Ture if the deque is empty."""
        return self._size == 0

    def first(self):
        """ Return (but do not remove) the element at the front of the queue.
        raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._data[self._front]

    def add_first(self, e):
        """ Add an element to the front of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def delete_first(self):
        """ Delete an element to the front of the deque.
        if the deque size is less than a quarter of underlying list capacity,
        then shrink list to half.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # shrink the list
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)

    def last(self):
        """ Return (but do not remove) the element at the last of the queue.
        raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        last = (self._front + self._size - 1) % len(self._data)
        return self._data[last]

    def add_last(self, e):
        """ Add an element to the back of the deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        last = (self._front + self._size - 1) % len(self._data)
        self._data[last + 1] = e
        self._size += 1

    def delete_last(self):
        """ Delete an element to the back of the deque.
        if the deque size is less than a quarter of underlying list capacity,
        then shrink list to half.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        last = (self._front + self._size - 1) % len(self._data)
        self._data[last] = None
        self._size -= 1
        # shrink the list
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)

    def _resize(self, cap):
        """ Resize to a new list of capacity `cap`."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

if __name__ == '__main__':
    d = ArrayDeque()
    for i in range(10):
        d.add_first(i)
    for i in range(10, 20):
        d.add_last(i)
    print(d._data)
    print('first: {0:d}'.format(d.first()))
    print('last: {0:d}'.format(d.last()))

    for i in range(5):
        d.delete_first()
    for i in range(5):
        d.delete_last()
    print(d._data)
    print('first: {0:d}'.format(d.first()))
    print('last: {0:d}'.format(d.last()))

    for i in range(20, 30):
        d.add_first(i)
    print(d._data)
    print('first: {0:d}'.format(d.first()))
    print('last: {0:d}'.format(d.last()))

    for i in range(15):
        d.delete_last()
    print(d._data)
    print('first: {0:d}'.format(d.first()))
    print('last: {0:d}'.format(d.last()))

    for i in range(30, 50):
        d.add_last(i)
    print(d._data)
    print('first: {0:d}'.format(d.first()))
    print('last: {0:d}'.format(d.last()))
    print('size: {0:d}, capacity: {1:d}'.format(len(d), len(d._data)))

