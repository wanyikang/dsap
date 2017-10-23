# -*- coding: utf-8 -*-
from transfer_r6_3 import ArrayStack

def reverse_list(l):
    s = ArrayStack()
    for item in l:
        s.push(item)
    for i in range(len(l)):
        l[i] = s.pop()

if __name__ == '__main__':
    l = [i for i in range(10)]
    print(l)
    reverse_list(l)
    print(l)

