# This the excise of r5.7
# array A contains integers from 1 to n-1, inclusive, with exactly on repeated,
# this algorithm is to find the integer in A that is repeated. And the running
# time of the algorithm is O(n).

# -*- coding: utf-8 -*-
import random
# array length
arr_len = 10

# make array a
a = arr_len * [None]
for i in range(1, arr_len):
    a[i] = i
# a[0] = random.randint(1, 99)
a[0] = 4
random.shuffle(a)

def find_repeated(a):
    """ algorithm that find the repeated element.
    :return : the value of the repeated element in array a
    """
    b = len(a) * [None]
    for i in range(len(a)):
        if b[a[i]] is None:
            b[a[i]] = 0
        else:
            break
    return a[i]


if __name__ == '__main__':
    v = find_repeated(a)
    print(a)
    print("the repeated integer is {0}".format(v))
