# -*- coding: utf-8 -*-
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

