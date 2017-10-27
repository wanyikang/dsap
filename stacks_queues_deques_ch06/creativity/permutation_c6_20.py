# -*- coding: utf-8 -*-
#
# the explain of algorithm by stack
#                             |  1  | x pop
#                             |-----|
#                             |  32 | x pop
#                             |-----| when top item is len one
# |  12 | x pop               |  2  | then concate the poped
# |-----|                     |-----| two items and is one
# |  3  | x pop               |  31 | result
# |-----| concate and push    |-----|
# |  13 |                     |  13 |                          |  13 |
# |-----|       ----->        |-----|          ----->          |-----|
# |  2  |                     |  2  |                          |  2  |
# |-----|                     |-----|                          |-----|
# |  23 |                     |  23 |      results:            |  23 |
# |-----|                     |-----|      [[3,2,1],[3,1,2]]   |-----|
# |  1  |                     |  1  |                          |  1  |
# initial
from array_stack_c6_16 import ArrayStack

def permutation_recursive(l):
    """ permutation by using recursive method."""
    length = len(l)
    if length == 0:
        return []
    elif length == 1:
        return [l[0:1]]
    else:
        perm = []
        for i in range(length):
            tmp = l[0:i] + l[i+1:]
            for item in permutation_recursive(tmp):
                perm.append(l[i:i+1] + item)
        return perm

def permutation_stack(l, s):
    """ permutation by using nonrecursive method, but with a stack."""
    length = len(l)
    # initialize the stack
    for i in range(length):
        s.push(l[i:i+1])
        s.push(l[:i] + l[i+1:])
    rlt = []
    # pop two element every time
    while(not s.is_empty()):
        top = s.pop()
        snd = s.pop()
        if len(top) > 1:
            for i in range(len(top)):
                s.push(snd + top[i:i+1])
                s.push(top[:i] + top[i+1:])
        else:
            rlt.append(snd + top)
    return rlt

if __name__ == '__main__':
    l = [i for i in range(1, 4)]
    s = ArrayStack()
    pr = permutation_recursive(l)
    print("pr length: {0:d}".format(len(pr)))
    print(pr)
    ps = permutation_stack(l, s)
    print("ps length: {0:d}".format(len(ps)))
    print(ps)

