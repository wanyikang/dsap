# -*- coding: utf-8 -*-
#
# Let l be the underlying list for storing the elements.
# Just notice that f(n) = g(n) - 1
#
# Algorithm root():
#   return l[1]
#
# Algorithm parent(p):
#   if p == 1:
#       return None
#   elif p-1 is odd:
#       return (p-1-1) // 2 + 1
#   else:
#       return (p-1-2) // 2 + 1
#
# Algorithm left(p):
#   return 2(p-1) + 1 +1
#
# Algorithm right(p):
#   return 2(p-1) + 2 + 1
#
# Algorithm is_leaf(p):
#   left = self.left(p)
#   right = self.right(p)
#   try:
#       if l[left] or l[right]:
#           rlt = True
#   except IndexError:
#       rlt = False
#   else:
#       rlt = False
#   return rlt
#
# Algorithm is_root(p):
#   return p == 1

