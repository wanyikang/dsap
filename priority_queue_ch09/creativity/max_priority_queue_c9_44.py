# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from priqueues.heap_priority_queue import HeapPriorityQueue

class MaxPriorityQueue(object):
    """ An implementation of maximum-oriented priority queue."""

    class _Key(object):
        """ Adaptor key for invert comparisons."""
        __slots__ = '_key'

        def __init__(self, key):
            self._key = key

        def __lt__(self, other):
            return self._key > other._key

    def __init__(self):
        self._data = HeapPriorityQueue()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def add(self, key, value):
        key = self._Key(key)
        self._data.add(key, value)

    def max(self):
        key, value = self._data.min()
        return (key._key,  value)

    def remove_max(self):
        key, value = self._data.remove_min()
        return (key._key, value)

if __name__ == '__main__':
    pq = MaxPriorityQueue()
    pq.add(0, 'richard')
    pq.add(0, 'wanyikang')
    pq.add(1, 'hsj')
    pq.add(2, 'mbs')
    pq.add(3, 'zzw')
    print('max: {0}, len: {1}'.format(pq.max(), len(pq)))
    pq.remove_max()
    print('max: {0}, len: {1}'.format(pq.max(), len(pq)))
    pq.remove_max()
    pq.remove_max()
    pq.remove_max()
    print('max: {0}, len: {1}'.format(pq.max(), len(pq)))

