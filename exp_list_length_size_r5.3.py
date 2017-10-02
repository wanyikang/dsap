# the exercise of r5.3

# -*- coding: utf-8 -*-
import sys

try:
    n = int(argv[1])
except:
    n = 1000

data = []
for _ in range(n):
    data.append(None)

for k in range(len(data)):
    pre_size = sys.getsizeof(data)
    data.pop()
    cur_size = sys.getsizeof(data)
    if pre_size != cur_size:
        print("k:{0}; pre_size:{1}; cur_size:{2}".format(k, pre_size, cur_size))
