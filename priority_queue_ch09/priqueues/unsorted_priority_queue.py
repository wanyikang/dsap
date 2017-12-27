# -*- coding: utf-8 -*-
from priority_queue_base import PriorityQueueBase
from collections.positional_list import PositionalList
from collections.exception import Empty

class UnsortedPriorityQueue(PriorityQueueBase):
    """ A min-oriented priority queue implemented with an unsorted list."""

    def __init__(self):
        """ Constructor method for priority queue."""
        self._data = PositionalList()

    def __len__(self):
        """ Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """ Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def _find_min(self):
        """ Return Position of item with minimum key."""
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def min(self):
        """ Return but do not remove (k,v) tuple with minimum key.

        raise Empty exception if empty.
        """
        small = self._find_min()
        item = small.element()
        return (item._key, item._value)

    def remove_min(self):
        """ Remove and return (k,v) tuple with minimum key.

        raise Empty excetion if empty
        """
        small = self._find_min()
        item = small.element()
        self._data.delete(small)
        return (item._key, item._value)

if __name__ == '__main__':
    pq = UnsortedPriorityQueue()
    pq.add(0, 'richard')
    pq.add(0, 'wanyikang')
    pq.add(1, 'hsj')
    pq.add(2, 'mbs')
    pq.add(3, 'zzw')
    print('min: {0}, len: {1}'.format(pq.min(), len(pq)))
    pq.remove_min()
    print('min: {0}, len: {1}'.format(pq.min(), len(pq)))
    pq.remove_min()
    pq.remove_min()
    pq.remove_min()
    print('min: {0}, len: {1}'.format(pq.min(), len(pq)))

