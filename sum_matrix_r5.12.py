# -*- coding: utf-8 -*-
# this is exercise 5.12
# I think sum is just do list comprehension twice

m = 8
n = 8
mx = [[i] * n for i in range(m)]
# sum all of the element
def sum_matrix(mx):
    subtotals = [sum(item) for item in mx]
    return sum(subtotals)

print(sum_matrix(mx))
