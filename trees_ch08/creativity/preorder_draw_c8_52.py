# -*- coding: utf-8 -*-
# when n=1, (0,0), all nodes coordinates are different
# when n=2, (0,0) (1,1), all nodes coordinates are different
# Asume when n=k, all nodes coordinates are different
# Let prove n=k+1, all nodes coordinates are different.
#
# First, we can add one extra node to the k nodes tree, and make extra node
# has the maximum depth(let extra node be a child of the original maximum
# depth leaf). So the extra node is different from all the original nodes
# because it has the maximum depth. Namely, all the coordinates of the new tree
# are different.
# Second, we can add one extra node to the k nodes tree, and make the depth of
# extra node not more than the original maximum depth. And the nodes before
# extra in the postorder traversal are the same coordinate, the nodes after
# extra get their x-coodination increased one, so all the coordinates of new
# tree are different.
#
# And There is only the above two circumstances, maximum depth not not. So we
# ge that when n=k+1, all nodes coordinates are different too.

