# -*- coding: utf-8 -*-
# this is exercise of c5.17
# prove the following operations takes O(n) time: n append operations on an
# initially empty array, followed by n pop operations

# From the result of this experiment, we can prove that the time is O(n).
# We can also analyse the append and pop method, we know append method is
# amortized O(1), pop method is just the reverse procedure of append, so
# is amortized time is O(1) too, then n append after n pop take time O(n).
import timeit
from dynamic_array_pop_c5_16 import DynamicArray

a = DynamicArray()

def func_test(n):
    for i in range(n):
        a.append(i)
    for i in range(n):
        a.pop()

try:
    for i in range(1, 7):
        cnt = 10 ** i
        func_s = "func_test(" + str(cnt) + ")"
        t = timeit.timeit(func_s, setup="from __main__ import func_test", number=1)
        print("cnt: {0:<10d},  time: {1:<.6f}".format(cnt, t / cnt))
except KeyboardInterrupt:
    print("\n")
    pass
except:
    pass
