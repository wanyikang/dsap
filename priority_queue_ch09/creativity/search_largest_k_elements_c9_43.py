# -*- coding: utf-8 -*-
# Build a tree with size k(not bottom-up contruct, just add a element one
# time), that takes k*logk time. And the add another one element to the tree
# one time, after bubbling, then delete the last element. That operation takes
# logk time, and n-k elements take (n-k)*logk time. So total time is
# k*logk + (n-k)*logk = n*logk, So is O(n*logk)

