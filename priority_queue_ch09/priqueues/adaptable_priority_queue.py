# -*- coding: utf-8 -*-
from heap_priority_queue import HeapPriorityQueue
from collections.exception import Empty

class AdaptablePriorityQueue(HeapPriorityQueue):
    """ A min-oriented priority queue implemented with a heap."""

    # nested class
    class Locator(HeapPriorityQueue._Item):
        """ Token for locating an entry of the priority queue."""
        __slots__ = '_index'  # add index as additional field

        def __init__(self, k, v, j):
            super(AdaptablePriorityQueue.Locator, self).__init__(k, v)
            self._index = j

    # public method
    def add(self, key, value):
        """ Add a key-value pair and return a locator token."""
        token = self.Locator(key, value, len(self))
        self._data.append(token)
        self._up_heap(len(self) - 1)
        return token

    def update(self, loc, newkey, newval):
        """ Update the key and value for the entry identified by Locator loc."""
        if not (0 <= loc._index < len(self) and loc is self._data[loc._index]):
            raise ValueError('Invaid locator')
        loc._key, loc._value = newkey, newval
        self._bubble(loc._index)

    def remove(self, loc):
        """ Remove and return the (k,v) pair identified by Locator loc."""
        if not (0 <= loc._index < len(self) and loc is self._data[loc._index]):
            raise ValueError('Invaid locator')
        if loc._index == len(self) - 1:
            token = self._data.pop()
        else:
            self._swap(loc._index, len(self) - 1)
            token = self._data.pop()
            self._bubble(loc._index)
        return (token._index, token._value)

    # utils
    def _swap(self, i, j):
        """ Swap the elements at indices i and j of array and reset the
        indices."""
        super(AdaptablePriorityQueue, self)._swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        """ If element at index j is lower than it's parent, then do up_heap.
        Otherwise, do down_heap."""
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._up_heap(j)
        else:
            self._down_heap(j)


if __name__ == '__main__':
    pq = AdaptablePriorityQueue()
    richard = pq.add(0, 'richard')
    pq.add(0, 'wanyikang')
    hsj = pq.add(1, 'hsj')
    mbs = pq.add(2, 'mbs')
    zzw = pq.add(3, 'zzw')
    print('min: {0}, len: {1}'.format(pq.min(), len(pq)))
    pq.update(hsj, -1, 'hsj')
    print('min: {0}, len: {1}'.format(pq.min(), len(pq)))
    pq.remove(zzw)
    print('min: {0}, len: {1}'.format(pq.min(), len(pq)))

