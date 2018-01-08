# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from priqueues.heap_priority_queue import HeapPriorityQueue

class PriorityQueue(HeapPriorityQueue):

    def _down_heap(self, j):
        """ Bubbling the element identified by `j` down."""
        while self._has_left(j):
            small = self._left(j)
            if self._has_right(j):
                right = self._right(j)
                if self._data[small] > self._data[right]:
                    small = right
            if self._data[j] <= self._data[small]:
                break
            self._swap(j, small)
            j = small


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

