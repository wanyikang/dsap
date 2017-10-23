# -*- coding: utf-8 -*-
from transfer_r6_3 import ArrayStack
def remove_all_from_stack(s):
    if len(s) == 0:
        return
    else:
        s.pop()
        remove_all_from_stack(s)

if __name__ == '__main__':
    s = ArrayStack()
    for i in range(300):
        s.push(i)
    print(s._data)
    remove_all_from_stack(s)
    print(s._data)

