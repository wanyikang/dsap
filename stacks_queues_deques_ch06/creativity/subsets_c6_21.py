# -*- coding: utf-8 -*-
from copy import copy
from array_stack_c6_16 import ArrayStack
from queue import MyQueue
def subsets(l):
    rlt = []
    s = ArrayStack()
    q = MyQueue()
    s.push([])
    s.push(l[0:1])
    for i in range(1, len(l)):
        while(not s.is_empty()):
            st = s.pop()
            q.enqueue(copy(st))
            st.append(l[i])
            q.enqueue(st)
        while(not q.is_empty()):
            st = q.dequeue()
            s.push(st)
    while(not s.is_empty()):
        st = s.pop()
        if st != []:
            rlt.append(st)
    return rlt

if __name__ == '__main__':
    l = [i for i in range(1, 5)]
    r = subsets(l)
    print(r)

