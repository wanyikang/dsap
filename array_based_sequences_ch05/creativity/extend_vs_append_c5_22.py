# -*- coding: utf-8 -*-
# This is exercise of c5.22.
# Develop an experiment to compare the relative efficiency of the extend method
# and the append method. Of course, use these two method to do the same work.
# From the result we can get the conclusion: extend is like about 20 times than
# append method
from timeit import timeit

def gen_an_array(alen):
    return [i for i in range(alen)]

def construct_by_append(a):
    tmp = []
    for item in a:
        tmp.append(item)

def construct_by_extend(a):
    tmp = []
    tmp.extend(a)

stp = """
from __main__ import gen_an_array
from __main__ import construct_by_append
from __main__ import construct_by_extend
a = gen_an_array(10^5 * 10000)
"""

if __name__ == '__main__':
    ttl = timeit("construct_by_append(a)", setup=stp, number=1000)
    print('construct_by_append: {0:.6f}'.format(ttl/1000))
    ttl = timeit("construct_by_extend(a)", setup=stp, number=1000)
    print('construct_by_extend: {0:.6f}'.format(ttl/1000))
