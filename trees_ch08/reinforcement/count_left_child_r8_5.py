# -*- coding: utf-8 -*-
# Algorithm count_left(T, p, cnt=0):
#     for each child c in T.children(p) do
#         cnt = count_left(T, c, cnt)
#     parent = T.parent(p)
#     if parent.left() is p and T.is_leaf():
#         return cnt += 1
#     else:
#         return cnt
#
# Actually, it is just an postorder traveral.

