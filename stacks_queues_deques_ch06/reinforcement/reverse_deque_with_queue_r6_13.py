# -*- coding: utf-8 -*-
from collections import deque
from my_queue_r6_11 import MyQueue
from exception import Empty

def reverse_deque(d, q):
    """ reverse a deque with queue, no other variables."""
    try:
        while True:
            elmnt = d.pop()
            q.enqueue(elmnt)
    except IndexError:
        pass

    try:
        while True:
            elmnt = q.dequeue()
            d.append(elmnt)
    except Empty:
        pass

if __name__ == "__main__":
    d = deque((1,2,3,4,5,6,7,8))
    print("original deque: ", d)
    q = MyQueue()
    reverse_deque(d,q)
    print("reversed deque: ", d)

