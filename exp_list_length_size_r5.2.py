# This is my answer of exercise r5.2
# output the value of k at which the existing capacity of array is exhausted

# -*- coding: utf-8 -*-
import sys

try:
    n = int(argv[1])
except:
    n = 100

data = []
for k in range(n):
    pre_size = sys.getsizeof(data)
    data.append(None)
    cur_size = sys.getsizeof(data)
    if pre_size != cur_size:
        print('length :k: {0}; Size in bytes: {1}'.format(k, pre_size))
