# -*- coding: utf-8 -*-
from positional_list_c7_36 import PositionalList
from random import shuffle

def bubble_sort(pl):
    """ Bubble sort for positional sort."""
    length = len(pl)
    if length == 0:
        return
    for i in range(length - 1, -1, -1):
        walk = pl.first()
        nxt = pl.after(walk)
        for j in range(i):
            if walk.element() > nxt.element():
                walk, nxt = swap(pl, walk, nxt)
                nxt = pl.after(walk)
            else:
                walk = nxt
                nxt = pl.after(nxt)
    return

def swap(pl, p, q):
    """ Swap position p and q in positional list `pl`."""
    if p and q:
        pe = pl.delete(p)
        new_p = pl.add_after(q, pe)
        return (new_p, q)
    return (p, q)

if __name__ == '__main__':
    pl = PositionalList()
    llen = 20
    l = [i for i in range(llen)]
    shuffle(l)
    for i in range(llen):
        pl.add_first(l[i])  # initialize pl to decreasing order
    print(pl)
    bubble_sort(pl)
    print(pl)

