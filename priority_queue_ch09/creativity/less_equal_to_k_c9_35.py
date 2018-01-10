# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from priqueues.heap_priority_queue import HeapPriorityQueue

class PriorityQueue(HeapPriorityQueue):

    def less_equal(self, k):
        """ Return the elements that having a key less than or equal to k."""
        rlt = []
        self._less_equal(0, k, rlt)
        return rlt

    def _less_equal(self, idx, k, rl):
        """ Append the elements that having a key less than or equal to `k` to
        `rl`."""
        item = self._data[idx]
        if item._key <= k:
            rl.append((item._key, item._value))
        if self._has_left(idx):
            self._less_equal(self._left(idx), k, rl)
        if self._has_right(idx):
            self._less_equal(self._right(idx), k, rl)


if __name__ == '__main__':
    elms = [(2,'B'), (5,'A'), (4,'C'), (15,'K'), (9,'F'), (7,'Q'), (6,'Z'),
            (16,'X'), (25, 'J'), (14,'E'), (12,'H'), (11,'S'), (8,'W'),
            (20,'B'), (10,'L')]
    pq = PriorityQueue(elms)
    lteqs = pq.less_equal(7)
    print(lteqs)

