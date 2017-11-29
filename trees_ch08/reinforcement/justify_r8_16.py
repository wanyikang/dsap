# -*- coding: utf-8 -*-
# a:
# For every position p in binary tree with height h, we have
# f(p) <= 2^0 + 2^1 + 2^2 + ... + 2^h -1 = 2^(h+1) - 1
# For a binary tree, every level at least has one node, so n >= h + 1
# So we get f(p) <= 2^(h+1) - 1 <= 2^n -2
#
# b:
# when the tree has only one element, we attains the upper bound.
#
