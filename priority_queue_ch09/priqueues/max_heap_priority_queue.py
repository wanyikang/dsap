# -*- coding: utf-8 -*-
from priority_queue_base import PriorityQueueBase
from collections.exception import Empty

class MaxHeapPriorityQueue(PriorityQueueBase):
    """ A max-oriented priority queue implemented with a heap."""

    # public methods
    def __init__(self, contents=()):
        """ Construct an empty priority queue."""
        self._data = [self._Item(k, v) for k,v in contents]  # empty by default
        if len(self._data) > 1:
            self._heapify()

    def __len__(self):
        """ Return the number of items in the priority queue."""
        return len(self._data)

    def is_empty(self):
        """ Return True if the priority queue is empty."""
        return len(self) == 0

    def add(self, key, value):
        """ Add a key-value pair."""
        self._data.append(self._Item(key, value))
        self._up_heap(len(self) - 1)

    def max(self):
        """ Return but do not remove (k,v) tuple with maximum key.

        raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)

    def remove_max(self):
        """ Remove and return (k,v) tuple with maximum key.

        raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty')
        self._swap(0, len(self) - 1)
        item = self._data.pop()
        self._down_heap(0)
        return (item._key, item._value)

    def heappushpop(self, key, value):
        """ Push (`key`, `value`) on the heap, then pop and return the biggest
        key-value pair from the heap."""
        if self.is_empty():
            return (key, value)
        big = self.max()
        if key > big[0]:
            return (key, value)
        # should return a different pair
        self._data[0]._key = key
        self._data[0]._value = value
        self._down_heap(0)
        return big

    def heapreplace(self, key, value):
        """ Pop and return the biggest key-value pair from the heap, and also
        push the new pair.

        Raise IndexError if the heap is empty.
        """
        if self.is_empty():
            raise IndexError('Priority queue is empty')
        big = self.max()
        self._data[0]._key = key
        self._data[0]._value = value
        self._down_heap(0)
        return big

    # utils
    def _parent(self, j):
        """ Return the index of parent."""
        return (j - 1) // 2

    def _left(self, j):
        """ Return the index of left child"""
        return 2 * j + 1

    def _right(self, j):
        """ Return the index of right child."""
        return 2 * j + 2

    def _has_left(self, j):
        """ Return True if has left child."""
        return (2 * j + 1) < len(self)

    def _has_right(self, j):
        """ Return True if has right child."""
        return (2 * j + 2) < len(self)

    def _swap(self, i, j):
        """ Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _up_heap(self, j):
        """ Bubbling the element identified by `j` up."""
        p = self._parent(j)
        if j > 0 and self._data[j] > self._data[p]:
            self._swap(j, p)
            self._up_heap(p)

    def _down_heap(self, j):
        """ Bubbling the element identified by `j` down."""
        if self._has_left(j):
            big = self._left(j)
            if self._has_right(j):
                right = self._right(j)
                if self._data[big] < self._data[right]:
                    big = right
            if self._data[j] < self._data[big]:
                self._swap(j, big)
                self._down_heap(big)
        return

    def _heapify(self):
        """ Do a bottom-up heap construction."""
        start = self._parent(len(self) - 1)
        for i in range(start, -1, -1):
            self._down_heap(i)

if __name__ == '__main__':
    l = [(0, 'richard'), (0, 'wanyikang'), (1, 'hsj'), (2, 'mbs'), (3, 'zzw')]
    pq = MaxHeapPriorityQueue(l)
    print('max: {0}, len: {1}'.format(pq.max(), len(pq)))
    pq.remove_max()
    print('max: {0}, len: {1}'.format(pq.max(), len(pq)))
    pq.remove_max()
    pq.remove_max()
    print('max: {0}, len: {1}'.format(pq.max(), len(pq)))
    item = pq.heappushpop(4, 'lcq')
    print('heappushpop: {0}, max: {1}, len" {2}'.format(
        item, pq.max(), len(pq)))
    item = pq.heapreplace(5, 'xxx')
    print('heappushpop: {0}, max: {1}, len" {2}'.format(
        item, pq.max(), len(pq)))

