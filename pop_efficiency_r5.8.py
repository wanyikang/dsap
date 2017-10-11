# -*- coding: utf-8 -*-

# This is the exercise of r5.8
# Experimentally evaluate the efficiency of the pop method of Python’s list class.
# It maybe take 10 minites to run this program.

import timeit
def statment_head(n):
    data = [None] * n
    for _ in range(n):
        data.pop(0)

def statment_middle(n):
    data = [None] * n
    for _ in range(n):
        data.pop(len(data) // 2)

def statment_tail(n):
    data = [None] * n
    for _ in range(n):
        data.pop()

if __name__ == '__main__':
    print("{0:<10s}{1:>10d}{2:>10d}{3:>10d}{4:>10d}{5:>10d}".format('N/A', 100, 1000, 10000, 100000, 1000000))
    num = 1
    # insert head
    ttl_100 = timeit.timeit("statment_head(100)", setup="from __main__ import statment_head", number=num)
    perop_100 = ttl_100 / num * 1000000 / 100  # unit: ms

    ttl_1000 = timeit.timeit("statment_head(1000)", setup="from __main__ import statment_head", number=num)
    perop_1000 = ttl_1000 / num * 1000000 / 1000  # unit: ms

    ttl_10000 = timeit.timeit("statment_head(10000)", setup="from __main__ import statment_head", number=num)
    perop_10000 = ttl_10000 / num * 1000000 / 10000  # unit: ms

    ttl_100000 = timeit.timeit("statment_head(100000)", setup="from __main__ import statment_head", number=num)
    perop_100000 = ttl_100000 / num * 1000000 / 100000  # unit: ms

    ttl_1000000 = timeit.timeit("statment_head(1000000)", setup="from __main__ import statment_head", number=num)
    perop_1000000 = ttl_1000000 / num * 1000000 / 1000000  # unit: ms
    print("{0:<10s}{1:>10.3f}{2:>10.3f}{3:>10.3f}{4:>10.3f}{5:>10.3f}".format(
        'k = 0', perop_100, perop_1000, perop_10000, perop_100000, perop_1000000))

    # insert middle
    ttl_100 = timeit.timeit("statment_middle(100)", setup="from __main__ import statment_middle", number=num)
    perop_100 = ttl_100 / num * 1000000 / 100  # unit: ms

    ttl_1000 = timeit.timeit("statment_middle(1000)", setup="from __main__ import statment_middle", number=num)
    perop_1000 = ttl_1000 / num * 1000000 / 1000  # unit: ms

    ttl_10000 = timeit.timeit("statment_middle(10000)", setup="from __main__ import statment_middle", number=num)
    perop_10000 = ttl_10000 / num * 1000000 / 10000  # unit: ms

    ttl_100000 = timeit.timeit("statment_middle(100000)", setup="from __main__ import statment_middle", number=num)
    perop_100000 = ttl_100000 / num * 1000000 / 100000  # unit: ms

    ttl_1000000 = timeit.timeit("statment_middle(1000000)", setup="from __main__ import statment_middle", number=num)
    perop_1000000 = ttl_1000000 / num * 1000000 / 1000000  # unit: ms
    print("{0:<10s}{1:>10.3f}{2:>10.3f}{3:>10.3f}{4:>10.3f}{5:>10.3f}".format(
        'k = n // 2', perop_100, perop_1000, perop_10000, perop_100000, perop_1000000))

    # insert tail
    ttl_100 = timeit.timeit("statment_tail(100)", setup="from __main__ import statment_tail", number=num)
    perop_100 = ttl_100 / num * 1000000 / 100  # unit: ms

    ttl_1000 = timeit.timeit("statment_tail(1000)", setup="from __main__ import statment_tail", number=num)
    perop_1000 = ttl_1000 / num * 1000000 / 1000  # unit: ms

    ttl_10000 = timeit.timeit("statment_tail(10000)", setup="from __main__ import statment_tail", number=num)
    perop_10000 = ttl_10000 / num * 1000000 / 10000  # unit: ms

    ttl_100000 = timeit.timeit("statment_tail(100000)", setup="from __main__ import statment_tail", number=num)
    perop_100000 = ttl_100000 / num * 1000000 / 100000  # unit: ms

    ttl_1000000 = timeit.timeit("statment_tail(1000000)", setup="from __main__ import statment_tail", number=num)
    perop_1000000 = ttl_1000000 / num * 1000000 / 1000000  # unit: ms
    print("{0:<10s}{1:>10.3f}{2:>10.3f}{3:>10.3f}{4:>10.3f}{5:>10.3f}".format(
        'k = n', perop_100, perop_1000, perop_10000, perop_100000, perop_1000000))

