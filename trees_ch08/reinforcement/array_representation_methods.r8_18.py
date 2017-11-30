# -*- coding: utf-8 -*-
# Let l be the underlying list for storing the elements.
# Algorithm root():
#   return l[0]
#
# Algorithm parent(p):
#   if p == 0:
#       return None
#   elif p is odd:
#       return (p-1) // 2
#   else:
#       return (p-2) // 2
#
# Algorithm left(p):
#   return 2p+1
#
# Algorithm right(p):
#   return 2p + 2
#
# Algorithm is_leaf(p):
#   left = 2p + 1
#   right = 2p + 2
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
#   return p == 0

