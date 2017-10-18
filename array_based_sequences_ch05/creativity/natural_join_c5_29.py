# -*- coding: utf-8 -*-
# This is exercise of c5.29
# Describe and analyze an efficient algorithm for computing the natural join of
# a list A of n pairs and a list B of m pairs.
#
# 1, use dual loops, the time is O(mn)
#
# 2, use auxiliary dict to make the time O(m+n). Iterate A and B respectively,
# and insert it's elements to the dic like below:
# y: [ [(x,y), ..., (z,y)], [(y,b), ..., (y,c)]]
# a: [ [(x,a), ..., (z,a)], [(a,b), ..., (a,c)]]
# ...
# z: [ [(x,z), ..., (z,z)], [(z,b), ..., (z,c)]]
#
# the first list of matrix is from A, and all it's elements are y end, the
# second list of matrix is from B, all all it's elements are y start.
# It will take O(m+n) time to do this. Then iterate the matrix to join every
# value repectively and append to another list. That will take O(m+n) time,
# because there is only m+n elements in the matrix. Thus we get the result in
# O(m+n) time

