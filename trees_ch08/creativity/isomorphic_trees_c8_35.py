# -*- coding: utf-8 -*-
# Algorithm is_isomorphic(t1, t2):
#   if t1.is_leaf() and t2.is_leaf():
#       return True
#   elif t1.is_leaf and not t2.is_leaf():
#       return False
#   elif not t1.is_leaf and t2.is_leaf():
#       return False
#   else:
#       c1 = t1.num_children()
#       c2 = t2.num_children()
#       if c1 != c2:
#           return False
#       else:
#           result = True
#           iter1 = t1.children()
#           iter2 = t2.children()
#           try:
#               result = result and is_isomorphic(iter1.next(), iter2.next())
#           except StopIteration:
#               pass
#           return result

