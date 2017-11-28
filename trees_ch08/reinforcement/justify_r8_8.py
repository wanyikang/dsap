# -*- coding: utf-8 -*-
# Let i denotes the number of internal nodes, e denotes the number of external
# nodes, n denotes the number of whole tree nodes. For a proper binary tree, we
# can get 2i + 1 = n. Let's prove it first.
#
# Justify 2i + 1 = n (level_n denotes nodes number of level n):
# * all level 1 nodes can be gotten by 2 * level_0
# * all level 2 nodes can be gotten by 2 * level_1
# * all level k nodes can be gotten by 2 * level_(k-1)
# So 2i + 1 is equal to n
#
# Let's go to prove the proposition 8.8:
# a:
# i = (n-1)/2, so e = n-i = (n+1)/2 for a proper binary tree with height h
# so, want the e be minimum, we gonna make the n be minimum. Obviously, let
# every level has two nodes will make the n minimum for height h. So we get
# 2h + 1 = n, so e = (n + 1)/2 = h + 1, that's the minimum e.
#
# b:
# e = (n + 1)/2, Making every level has maximum nodes will lead the number n
# maximum. The maximum n for height h is (2^0 + 2^1 + ... + 2^h) = n
# n = 2^(h+1) - 1, so e = (n + 1)/2 = 2^h
#
# c:
# let n be the number of a proper binary tree, so the maximum height is case a,
# the minimum height is case b.
# Max height: h = (n-1)/2
# Min height: (2^0 + 2^1 + ... + 2^h) = n, h = log(n+1) - 1
# So we get log(n+1)-1 <= h <= (n-1)/2
#
# d:
# h = (n-1)/2: h = 3, n = 7 (every internal node has at most one child be
# internal node)
# h = log(n+1)-1: h=2, n=7 (every level has maximum nodes)

