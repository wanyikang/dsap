# -*- coding: utf-8 -*-
from priority_queue_base import PriorityQueueBase
from collections.positional_list import PositionalList
from collections.exception import Empty

class SortedPriorityQueue(PriorityQueueBase):
    """ A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """ Constructor method for priority queue."""
        self._data = PositionalList()

    def __len__(self):
        """ Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """ Add a key-value pair."""
        item = self._Item(key, value)
        walk = self._data.first()
        while walk and walk.element() <= item:
            walk = self._data.after(walk)
        if not walk:
            self._data.add_last(item)
        else:
            self._data.add_before(walk, item)
        return

    def min(self):
        """ Return but do not remove (k,v) tuple with minimum key.

        raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data.first().element()
        return (item._key, item._value)

    def remove_min(self):
        """ Remove and return (k,v) tuple with minimum key.

        raise Empty excetion if empty
        """
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)

if __name__ == '__main__':
    pq = SortedPriorityQueue()
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
    # pq.remove_min()
    print('min: {0}, len: {1}'.format(pq.min(), len(pq)))

