# -*- coding: utf-8 -*-
from collections import deque
from transfer_r6_3 import ArrayStack
from exception import Empty

def reverse_deque(d, s):
    """ reverse a deque with stack, no other variables."""
    try:
        while True:
            elmnt = d.pop()
            s.push(elmnt)
    except IndexError:
        pass

    try:
        while True:
            elmnt = s.pop()
            d.appendleft(elmnt)
    except Empty:
        pass

if __name__ == "__main__":
    d = deque((1,2,3,4,5,6,7,8))
    print("original deque: ", d)
    s = ArrayStack()
    reverse_deque(d,s)
    print("reversed deque: ", d)

