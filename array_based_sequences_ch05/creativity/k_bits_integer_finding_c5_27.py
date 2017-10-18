# -*- coding: utf-8 -*-
# This is exercise of c5.27
# Given a Python list L of n positive integers, each represented with
# k = ⎡ logn⎤ + 1 bits, describe an O(n)-time method for finding a k-bit
# integer not in L.
#
# Let's draw a table below(the index starts from 1):
#    index    bits
#       1       1
#       2       2
#       3       3
#       4       3
#       5       4
#       6       4
#       7       4
#       8       4
#       9       5
#       10      5
#       11      5
#       12      5
#       13      5
#       14      5
#       15      5
#       16      5
#       17      6
#
# So, the relationship between k and n is: k = ⎡ logn⎤ + 1. Look at the table,
# if given a specified k, the repective n must be in a range, let's get the
# range by math.
# k = ⎡ logn⎤ + 1
# 2^k = 2^(⎡ logn⎤ + 1)
# 2^(k-1) = 2^⎡ logn⎤
# # logn + 1 >= ⎡ logn⎤ >= logn, so 2^(logn + 1) >= 2^⎡ logn⎤ >= 2^logn
# 2^(logn + 1) >= 2^(k-1) >= 2^logn
# 2n >= 2^(k-1) >= n
# 2^(k-2) <= n <= 2^(k-1)
# So, for a specified k, the respectively n lays in [2^(k-2), 2^(k-1)], than we
# can write an program to iterate index from 2^(k-2) to 2^(k-1) to find the
# integer is exist or not. 2^(k-1) - 2^(k-2) = 2^(k-2) = 2^(⎡ logn⎤ - 1) >= n/2
# So the totle time T(n) >= n/2, namely Ω(n)
