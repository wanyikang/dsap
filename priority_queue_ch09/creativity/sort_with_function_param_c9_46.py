# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from random import shuffle
from priqueues.heap_priority_queue import HeapPriorityQueue as PriorityQueue
from priqueues.collections.positional_list import PositionalList

def pq_sort(C, func=None):
    """ Sort a collection of elements stored in a positional list."""
    n = len(C)
    P = PriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        if callable(func):
            key = func(element)
        P.add(key, element)
    for j in range(n):
        (k, v) = P.remove_min()
        C.add_last(v)

def make_key(k):
    return int(k)

if __name__ == '__main__':
    l = []
    for i in range(10):
        l.append(i)
    shuffle(l)
    pl = PositionalList()
    for item in l:
        pl.add_last(str(item))
    print(pl)
    pq_sort(pl, func=make_key)
    print(pl)

