# -*- coding: utf-8 -*-
# This is exercise of c5.25
# Implement a function with signature remove_all(data, value)
# We can't repeat call remove method of list, because if all the elements in
# data is the exactly same as value, then the worst-case time is O(n^2).
# So we use a new list, and append the element that is not equal to value to
# the new list by only one iteration of the data.
from timeit import timeit

def repeat_remove_all(data, value):
    """ Remove all the value by repeated call remove."""
    repeat = 0
    for i in range(len(data)):
        if data[i] == value:
            repeat += 1
    for i in range(repeat):
        data.remove(value)
    return data

def remove_all(data, value):
    """ Remove all the value by appending to a new list."""
    newa = []
    for item in data:
        if item != value:
            newa.append(item)
    return newa

def gen_array():
    value = 88888
    alen = 100000
    a = [i for i in range(alen // 2 + 1)]
    b = [value for i in range(alen // 2 + 1, alen)]
    a.extend(b)
    return a

stp_base = """
from __main__ import repeat_remove_all
from __main__ import remove_all
from __main__ import gen_array
data = gen_array()
value = 88888
"""

if __name__ == '__main__':
    ttl = timeit("remove_all(data, value)", setup=stp_base, number=1)
    print("remove_all: {0:.6f}".format(ttl))
    ttl = timeit("repeat_remove_all(data, value)", setup=stp_base, number=1)
    print("repeat_remove_all: {0:.6f}".format(ttl))

