# -*- coding: utf-8 -*-
from random import shuffle

def insert_sort(l):
    """ In-palce insert sort."""
    walk = 0
    while walk < len(l):
        i = walk + 1
        j = i - 1
        while  0 < i < len(l):
            if l[i] < l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
            i -= 1
            j = i - 1
        walk += 1
    return

if __name__ == "__main__":
    l = [i for i in range(10)]
    shuffle(l)
    print(l)
    insert_sort(l)
    print(l)

