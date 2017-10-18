# -*- coding: utf-8 -*-
# This is exercise of c5.24
# Do experiment to evaluate the efficiency of remove method of list class.
# From the result we get the conclusion: all remove method is amortized
# O(n), but the remove_from_head is fastest, remove_from_tail is slowest,
# and is about 20 times between them.
from timeit import timeit

def remove_from_head(a):
    alen = len(a)
    for i in range(alen):
        a.remove(a[0])

def remove_from_middle(a):
    alen = len(a)
    for i in range(alen):
        a.remove(a[len(a) // 2])

def remove_from_tail(a):
    alen = len(a)
    for i in range(alen):
        a.remove(a[-1])

def gen_an_array_list_comp(alen):
    return [i for i in range(alen)]

stp_base = """
from __main__ import remove_from_head
from __main__ import remove_from_middle
from __main__ import remove_from_tail
from __main__ import gen_an_array_list_comp
"""

if __name__ == '__main__':
    tnum = 1
    print("{0:>10s}    {1:s}    {2:s}".format("method", "alen(0.1k)", "time"))
    for i in range(4):
        stp = stp_base + "a = gen_an_array_list_comp(" + str(10**i *100) + ")"
        ttl = timeit("remove_from_head(a)", setup=stp, number=1)
        print("{0:>10}    10^{1:<8d}{2:.6f}".format("head", i, ttl/tnum))
        ttl = timeit("remove_from_middle(a)", setup=stp, number=1)
        print("{0:>10}    10^{1:<8d}{2:.6f}".format("middle", i, ttl/tnum))
        ttl = timeit("remove_from_tail(a)", setup=stp, number=1)
        print("{0:>10}    10^{1:<8d}{2:.6f}".format("tail", i, ttl/tnum))
        print("")

