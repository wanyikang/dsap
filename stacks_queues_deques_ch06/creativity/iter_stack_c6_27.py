# -*- coding: utf-8 -*-
from array_stack_c6_16 import ArrayStack
from queue import MyQueue

def find_element(stack, e):
    rlt = False
    q = MyQueue()
    for i in range(len(stack)):
        item = stack.pop()
        if item == e:
            rlt = True
        q.enqueue(item)
    [stack.push(q.dequeue()) for i in range(len(q))]
    [q.enqueue(s.pop()) for i in range(len(stack))]
    [stack.push(q.dequeue()) for i in range(len(q))]
    return rlt

if __name__ == '__main__':
    s = ArrayStack()
    for i in range(10):
        s.push(i)
    print('before: ', s._data)
    e = 5
    flag = find_element(s, e)
    print('{0:d} is in stack'.format(e))
    print('after: ', s._data)

