# -*- coding: utf-8 -*-
# Let e be the number of external nodes of binary tree T. let i be the number
# of internal nodes of tree T. Let i1 be the number of internal nodes that only
# have one child, let i2 be the number of internal nodes that have two
# children. Let n be the number of all nodes of tree T. So we get
# e + i1 + i2 = n. Let us make the tree T a proper binary tree with additional
# i1 counts of nodes, namely, all the i1 nodes of T get another leaf node, and
# we get a new proper binary tree T'.
# Within T, we get e + i1 + i2 = n, Within T', we have
# e + i1 + i2 + i1 = n + i1. Because T' is proper, External nodes is one more
# than internal nodes for proper trees. So we get e + i1 = i1 + i2 + 1.
# And that means 2(i1 + i2) = n-1+i1, i = (n-1+i1)/2.
# So if we want internal nodes of T is minimum, we just make the i1 minimum,
# and if we wantt internal nodes of T is maximum, we just make the i1 maximum.
# Then we get the following conclusions:
# max internal: n-1        min external: 1 (all node has at most 1 child)
# min internal: (n-1)/2    max external: (n+1)/2 (proper binary tree)

