# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from priqueues.heap_priority_queue import HeapPriorityQueue

class PriorityQueue(HeapPriorityQueue):

    def _up_heap(self, j):
        """ Bubbling the element identified by `j` up."""
        p = self._parent(j)
        while j > 0 and self._data[j] < self._data[p]:
            self._swap(j, p)
            j = p
            p = self._parent(j)

if __name__ == '__main__':
    pq = PriorityQueue()
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

