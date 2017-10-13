# -*- coding: utf-8 -*-
# this is exercise c5.14
# implement your own shuffle function.

import random

def my_shuffle(a):
    b = []
    flags = [None for _ in range(len(a))]
    # generage the shuffled indexes
    while True:
        idx = random.randrange(0, len(a))
        if flags[idx] is not None:
            continue
        else:
            flags[idx] = idx
            b.append(idx)
        if len(b) == len(a):
            break
    # shuffle array a
    for i in range(len(a)):
        a[i], a[b[i]] = a[b[i]], a[i]

if __name__ == '__main__':
    a = [i for i in range(20)]
    print(a)
    my_shuffle(a)
    print(a)

