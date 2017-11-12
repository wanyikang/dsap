# -*- coding: utf-8 -*-
from positional_list import PositionalList

def max(pl):
    """ Return the max element of the positional list pl. Return None if the
    list is empty."""
    if pl.is_empty():
        return None
    rlt = pl.first().element()
    for item in pl:
        if item > rlt:
            rlt = item.element()
    return rlt

if __name__ == '__main__':
    pl = PositionalList()
    for i in range(10000):
        pl.add_first(i)
    print('max: {0:d}'.format(max(pl)))

