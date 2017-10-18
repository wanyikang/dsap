# -*- coding: utf-8 -*-
# This is exercise of c5.26
#
# Describe a good algorithm for finding the repeated five integers in the list.
# 1, you can sort the list, then iterate it to check if there are continuous
# two elements are same value.
# 2, you can initailize a new array with length n-4 and all elements have None
# value, then iterate the original array, and insert the element to new array
# by using the value of the element as the index of new array.
from timeit import timeit
import random

def find_repeated(a):
    rlt = []
    b = [None] * (len(a) - 4)
    for i in range(len(a)):
        if b[a[i]] is None:
            b[a[i]] = 1
        else:
            rlt.append(a[i])
    return rlt

def find_repeated_by_sort(a):
    rlt = []
    a.sort()
    random.shuffle(a)
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            rlt.append(a[i])
    return rlt

def gen_array(alen):
    a = [i for i in range(1, alen + 1)]
    for i in range(1, 6):
        a[-i] = i
    return a

stp_base = """
from __main__ import find_repeated
from __main__ import find_repeated_by_sort
from __main__ import gen_array
a = gen_array(10**2 * 10000)
"""

if __name__ == '__main__':
    tnum = 10
    ttl = timeit("find_repeated(a)", setup=stp_base, number=tnum)
    print("find_repeated: {0:.8f}".format(ttl))
    ttl = timeit("find_repeated_by_sort(a)", setup=stp_base, number=tnum)
    print("find_repeated_by_sort: {0:.8f}".format(ttl))

