# This is the experiment of code fragment 5.1 of book data structures and
# algorithms in python.

# -*- coding: utf-8 -*-
import sys

try:
    n = int(argv[1])
except:
    n = 27

data = []
for _ in range(n):
    length = len(data)
    size = sys.getsizeof(data)
    data.append(None)
    print('Length: {0}; Size in bytes: {1}'.format(length, size))
