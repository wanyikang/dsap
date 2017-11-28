# -*- coding: utf-8 -*-
# Let i denotes the number of internal nodes, e denotes the number of external
# nodes, n denotes the number of whole tree nodes, ik means number of internal
# nodes in k level, and the maximum level is l. the tree is a proper binary
# tree.
#
# * all level 1 nodes can be gotten by 2 * level_0
# * all level 2 nodes can be gotten by 2 * level_1
# * all level k nodes can be gotten by 2 * level_(k-1)
# So 1 + 2*i0 + 2*i1 + 2*i2 + ... + 2*ik = n,
# n = 1 + 2*(i0 + i1 + i2 + ... + i(l-1)), n = 1 + 2i
# i = (n-1)/2, e = n-i = (n+1)/2
# so e = i + 1

