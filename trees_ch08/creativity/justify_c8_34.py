# -*- coding: utf-8 -*-
# Let the tree has k levels, and e denotes the number of all the external
# nodes, and i denotes the number of all the internal nodes, ik denotes the
# number of internal nodes at level k. We already have:
# i + e = n, i = i0+i1+i2+...+i(k-1)
#
# the number of nodes at level 1 is: 3*i0
# the number of nodes at level 2 is: 3*i1
# the number of nodes at level 3 is: 3*i2
# ...
# the number of nodes at level k is: 3*i(k-1)
# So n = 1+3*i0+3*i1+3*i2+...+3*i(k-1) = 1+3(i0+i1+i2+...+i(k-1)) = 1+3i
# So e = n-i = 3i+1-i = 2i+1

