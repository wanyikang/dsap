# -*- coding: utf-8 -*-
# This is exercise of c5.23.
# Develop an experiment to compare the relative efficiency of the list
# comprehension and the append method by using these two method to construct
# an array.
# From the result we get the conclusion: the comprehension is about 2 times
# fast than the append method.
from timeit import timeit

def gen_an_array_list_comp(alen):
    return [i for i in range(alen)]

def gen_an_array_append(alen):
    tmp = []
    for i in range(alen):
        tmp.append(i)

stp_base = """
from __main__ import gen_an_array_list_comp
from __main__ import gen_an_array_append
"""

if __name__ == '__main__':
    tnum = 1
    print("{0:>10s}    {1:s}    {2:s}".format("method", "arr_len", "time"))
    for i in range(5):
        stp = stp_base + "alen = " + str(10**i * 10000)
        ttl = timeit("gen_an_array_list_comp(alen)", setup=stp, number=tnum)
        print("{0:>10}    10^{1:d}    {2:.6f}".format("list_comp", i, ttl/tnum))
        ttl = timeit("gen_an_array_append(alen)", setup=stp, number=tnum)
        print("{0:>10}    10^{1:d}    {2:.6f}".format("append", i, ttl/tnum))
        print('')
