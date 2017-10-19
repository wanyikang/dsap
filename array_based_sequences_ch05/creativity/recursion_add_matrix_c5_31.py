# -*- coding: utf-8 -*-
# This is exercise of c5.31
# Describe a way to use recursion to add all the numbers in an n × n data set,
# represented as a list of lists.
# I use sum method for individual list, because I don't want to make the call
# stack too deep.
def gen_matrix(r, c):
    return [[i] * c for i in range(r)]

def sum_matrix(m, start, stop):
    """ Recursion add the matrix.
    :param start: the start index of matrix
    :param stop: the length of the matrix
    """
    rlt = 0
    if start >= stop:
        return 0
    elif start == stop - 1:
        return sum(m[start])
    else:
        mid = (start + stop) // 2
        rlt = sum_matrix(m, start, mid) + sum_matrix(m, mid, stop)
    return rlt

if __name__ == "__main__":
    m = gen_matrix(4000, 5000)
    rlt = sum_matrix(m, 0, len(m))
    print(rlt)
