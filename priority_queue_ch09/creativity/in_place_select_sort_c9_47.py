# -*- coding: utf-8 -*-
from random import shuffle

def selection_sort(l):
    """ In place selection sort."""
    walk = 0
    while walk < len(l):
        i = walk
        while i < len(l):
            if l[i] < l[walk]:
                # swap i and walk
                tmp = l[walk]
                l[walk] = l[i]
                l[i] = tmp
            i += 1
        walk += 1
    return

if __name__ == '__main__':
    l = []
    for i in range(10):
        l.append(i)
    shuffle(l)
    print(l)
    selection_sort(l)
    print(l)

