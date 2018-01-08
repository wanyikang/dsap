# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from priqueues.priority_queue_base import PriorityQueueBase
from priqueues.collections.exception import Empty

class SortedPriorityQueue(PriorityQueueBase):
    """ A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """ Constructor method for priority queue."""
        self._data = []

    def __len__(self):
        """ Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """ Add a key-value pair."""
        item = self._Item(key, value)
        self._data.append(item)
        idx = -1
        while idx >= (-1 * len(self)):
            pre_idx = idx - 1
            if pre_idx < (-1 * len(self)):
                break
            # swap idx and pre
            if self._data[idx] > self._data[pre_idx]:
                tmp = self._data[idx]
                self._data[idx] = self._data[pre_idx]
                self._data[pre_idx] = tmp
            idx -= 1
        return

    def min(self):
        """ Return but do not remove (k,v) tuple with minimum key.

        raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data[-1]
        return (item._key, item._value)

    def remove_min(self):
        """ Remove and return (k,v) tuple with minimum key.

        raise Empty excetion if empty
        """
        if self.is_empty():
            raise Empty('Priority queue is empty')
        item = self._data.pop()
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

