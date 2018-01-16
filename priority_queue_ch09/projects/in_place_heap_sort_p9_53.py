# -*- coding: utf-8 -*-
# the print info is as following:
#             10            100           1000          10000         100000
#          0.107          2.375         30.310        415.037       5407.535
#          0.095          1.933         28.986        416.099       5354.025
# and I think the conclusion is that the in place version is a little bit faster.

import sys
sys.path.append('..')
from priqueues.heap_priority_queue import HeapPriorityQueue
from priqueues.max_heap_priority_queue import MaxHeapPriorityQueue
from random import shuffle
import timeit

def pq_sort(L):
    """ Sort a collection of elements stored in a python list."""
    n = len(L)
    P = HeapPriorityQueue()
    for j in range(n):
        P.add(L[j], L[j])  # use element as key and value
    for j in range(n):
        (k,v) = P.remove_min()
        L[j] = v
    return

def pq_sort_in_place(L):
    """ Sort a collection of elements stored in a python list in place."""
    n = len(L)
    for i in range(n):
        L[i] = (L[i], L[i])  # use element as both key and value
    P = MaxHeapPriorityQueue(L)  # use bottom-up heap construction
    for j in range(n):
        (k,v) = P.remove_max()
        L[n-1-j] = v
    return


if __name__ == '__main__':
    l = []
    times = (10, 100, 1000, 10000, 100000)
    for item in times:
        tmp = [i for i in range(item)]
        shuffle(tmp)
        l.append(tmp)

    num = 2
    print("{0:>15d}{1:>15d}{2:>15d}{3:>15d}{4:>15d}".format(10, 100,
        1000, 10000, 100000))
    ttl_10 = timeit.timeit('pq_sort(list(l[0]))',
            setup='from __main__ import pq_sort; from __main__ import l', number=num)
    perop_10 = ttl_10 / num * 1000  # unit: ms

    ttl_100 = timeit.timeit('pq_sort(list(l[1]))',
            setup='from __main__ import pq_sort; from __main__ import l', number=num)
    perop_100 = ttl_100 / num * 1000  # unit: ms

    ttl_1000 = timeit.timeit('pq_sort(list(l[2]))',
            setup='from __main__ import pq_sort; from __main__ import l', number=num)
    perop_1000 = ttl_1000 / num * 1000  # unit: ms

    ttl_10000 = timeit.timeit('pq_sort(list(l[3]))',
            setup='from __main__ import pq_sort; from __main__ import l', number=num)
    perop_10000 = ttl_10000 / num * 1000  # unit: ms

    ttl_100000 = timeit.timeit('pq_sort(list(l[4]))',
            setup='from __main__ import pq_sort; from __main__ import l', number=num)
    perop_100000 = ttl_100000 / num * 1000  # unit: ms
    print("{0:>15.3f}{1:>15.3f}{2:>15.3f}{3:>15.3f}{4:>15.3f}".format(
        perop_10, perop_100, perop_1000, perop_10000, perop_100000))

    ttl_10 = timeit.timeit('pq_sort_in_place(list(l[0]))',
            setup='from __main__ import pq_sort_in_place; from __main__ import l', number=num)
    perop_10 = ttl_10 / num * 1000  # unit: ms

    ttl_100 = timeit.timeit('pq_sort_in_place(list(l[1]))',
            setup='from __main__ import pq_sort_in_place; from __main__ import l', number=num)
    perop_100 = ttl_100 / num * 1000  # unit: ms

    ttl_1000 = timeit.timeit('pq_sort_in_place(list(l[2]))',
            setup='from __main__ import pq_sort_in_place; from __main__ import l', number=num)
    perop_1000 = ttl_1000 / num * 1000  # unit: ms

    ttl_10000 = timeit.timeit('pq_sort_in_place(list(l[3]))',
            setup='from __main__ import pq_sort_in_place; from __main__ import l', number=num)
    perop_10000 = ttl_10000 / num * 1000  # unit: ms

    ttl_100000 = timeit.timeit('pq_sort_in_place(list(l[4]))',
            setup='from __main__ import pq_sort_in_place; from __main__ import l', number=num)
    perop_100000 = ttl_100000 / num * 1000  # unit: ms
    print("{0:>15.3f}{1:>15.3f}{2:>15.3f}{3:>15.3f}{4:>15.3f}".format(
        perop_10, perop_100, perop_1000, perop_10000, perop_100000))

