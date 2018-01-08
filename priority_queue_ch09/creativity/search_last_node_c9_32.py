# -*- coding: utf-8 -*-
# Let last be the reference of last node. p be the reference of parent node of
# last. Do simple up-and-down searches in the tree to locate the last node each
# time.
#
# For add, if right child of p is last, then make p be last, and do the
# aboving step again untile p is root or p.right() is not last, then let last
# be the sibling of last, and get the left of last until a leaf.
#
# For remove_min, the procedure is very similar, following is the algorithm:
# Algorithm search_last_node(t, walk, up=True):
#   if len(t) == 0 or len(t) == 1:
#       return None
#   elif len(t) == 2:
#       return t.root()
#   elif up:
#       p = t.parent(walk)
#       if p is t.root():
#           walk = t.sibling(walk)
#           return search_last_node(t, walk, False)
#       elif t.left(p) is walk:
#           return search_last_node(t, p)
#   else:
#       if t.is_leaf(walk):
#           return walk
#       elif t.right(walk):
#           walk = t.right(walk)
#       else:
#           walk = t.left(walk)
#       return search_last_node(t, walk, False)

