# -*- coding: utf-8 -*-
# The depth of p can also be recursively defined as follows:
# * If pistheroot,thenthedepthof p is 0.
# * Otherwise, the depth of p is one plus the depth of the parent of p.
#
# The height of a position p in a tree T is also defined recursively:
# * If p is a leaf, then the height of p is 0.
# * Otherwise, the height of p is one more than the maximum of the heights of
# p’s children.
# The height of a nonempty tree T is the height of the root of T.
#
# From the definition of height of tree we can know that the height of nonempty
# tree is the longest path in the tree. That means the longest path of
# root-external paths.
# From the definition of depth we can know that the depth of a leaf node is a
# path of the tree.
# And we know that the external node is leaf, so we can get propositon 8.4

