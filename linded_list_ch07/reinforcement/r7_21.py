# -*- coding: utf-8 -*-
# Assume the list means python list, not mtf list, and the list is maintained
# by mtf. So the following swquences takes Ω(n^3) for mtf:
# for _ in range(n):
#    for idx in range(-1, -n-1, -1):
#        mtf.access(list[idx])
#
# the inner loop is iterate the list in reverse order, for every access, it
# needs Ω(n) time, So the whole inner loop needs Ω(n^2) time, so the whole code
# segment needs Ω(n^3).

