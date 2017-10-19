# -*- coding: utf-8 -*-
# This is exercise of p5.33
# Write a Python program for a matrix class that can add and multiply two-
# dimensional arrays of numbers.
class Matrix(object):
    def __init__(self, r, c, empty=True):
        super(Matrix, self).__init__()
        self._row = r
        self._column = c
        if empty:
            self._m = self._construct_empty_matrix(r, c)
        else:
            self._m = self._construct_matrix(r, c)

    def __getitem__(self, key):
        """ Override indexing method."""
        return self._m[key]

    def __len__(self):
        """ Override len method."""
        return len(self._m)

    def _construct_empty_matrix(self, r, c):
        return [[None] * c for i in range(r)]

    def _construct_matrix(self, r, c):
        return [[i + 1] * c for i in range(r)]

    def add(self, m):
        rlt = self._construct_empty_matrix(self._row, self._column)
        # check dimensions agree
        if not m or not m[0]:
            print("Illegal parameter m!")
            return None
        if self._row != len(m) or self._column != len(m[0]):
            print("Illegal parameter m!")
            return None
        # double loop
        for i in range(self._row):
            for j in range(self._column):
                rlt[i][j] = self._m[i][j] + m[i][j]
        return rlt

    def scalar_multiple(self, c):
        rlt = self._construct_empty_matrix(self._row, self._column)
        # check if c is a constant
        if type(c) is not integer:
            print("Illegal parameter c!")
            return None
        # double loop
        for i in range(self._row):
            for j in range(self._column):
                rlt[i][j]= c * self._m[i][j]
        return rlt

    def dot_multiple(self, m):
        rlt = self._construct_empty_matrix(self._row, len(m[0]))
        # check dimensions agree
        if not m or not m[0]:
            print("Illegal parameter m!")
            return None
        if self._column != len(m):
            print("Illegal parameter m!")
            return None
        # triple loop
        s = self._m
        for i in range(self._row):
            for j in range(len(m[0])):
                ttl = 0
                for k in range(self._column):
                    ttl += s[i][k] * m[k][j]
                rlt[i][j] = ttl
        return rlt

if __name__ == "__main__":
    m1 = Matrix(3, 3, False)
    m2 = Matrix(3, 3, False)
    m_add = m1.add(m2)
    print(m_add)
    m1 = Matrix(3, 2, False)
    m2 = Matrix(2, 4, False)
    m_dot = m1.dot_multiple(m2)
    print(m_dot)

