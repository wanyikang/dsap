# -*- coding: utf-8 -*-
# n, level number, path, binary expansion
# 13    12      101     1101
# 14    13      110     1110
# 15    14      111     1111
#
# The path to the last node in the heap is given by the path represented by the
# binary expansion of n with the highest-order bit removed. And it takes O(1)
# time.
# When we get the path, we need to follow the path the reach the last node, it
# takes O(logn) time.

