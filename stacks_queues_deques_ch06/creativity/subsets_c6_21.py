# -*- coding: utf-8 -*-
from copy import copy
from array_stack_c6_16 import ArrayStack
from queue import MyQueue

def subsets_recursive(l):
    rlt = []
    length = len(l)
    if not l:
        return []
    elif length == 1:
        return [l, []]
    else:
        reduced_l = l[1:]
        rm_elmnt = l[0:1]
        subs = subsets_recursive(reduced_l)
        for item in subs:
            rlt.append(item)
            tmp = copy(item)
            tmp.extend(rm_elmnt)
            rlt.append(tmp)
        return rlt

def subsets_stack(l):
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
    l = [i for i in range(1, 3)]
    rs = subsets_stack(l)
    print("subsets_stack: ", rs)
    rr = subsets_recursive(l)
    rr.remove([])
    print("subsets_recursive: ", rr)

