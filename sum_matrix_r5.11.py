# -*- coding: utf-8 -*-
# this is exercise 5.11

m = 8
n = 8
mx = [[i] * n for i in range(m)]
# sum all of the element
sum = 0
for i in range(m):
    for j in range(n):
        sum += mx[i][j]
print('sum of matrix is: {0:d}'.format(sum))
