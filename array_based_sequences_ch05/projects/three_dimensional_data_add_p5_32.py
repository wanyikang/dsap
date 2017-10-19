# -*- coding: utf-8 -*-
# This is exercise of c5.32
# Write a Python function that takes two three-dimensional numeric data sets
# and adds them componentwise.
def gen_matrix(r, c):
    return [[i] * c for i in range(r)]

def gen_three_dimensional_data_set(x, y, z):
    triple = []
    for i in range(z):
        m = gen_matrix(y, x)
        triple.append(m)
    return triple

def triple_add(t1, t2):
    z = len(t1)
    y = len(t1[0])
    x = len(t1[0][0])
    rlt = gen_three_dimensional_data_set(x, y, z)
    for i in range(z):
        for j in range(y):
            for k in range(x):
                rlt[i][j][k] = t1[i][j][k] + t2[i][j][k]
    return rlt

if __name__ == '__main__':
    t1 = gen_three_dimensional_data_set(3, 3, 4)
    t2 = gen_three_dimensional_data_set(3, 3, 4)
    t = triple_add(t1, t2)
    print(t)

