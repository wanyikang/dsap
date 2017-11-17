# -*- coding: utf-8 -*-
from positional_list import PositionalList

def find_sum_v_elements(pl, v):
    """ Find the elements in the positional list that sums to v.

    :param pl: nondecreasing sorted positional list
    :param v: the demanded sum v
    """
    head = pl.first()
    tail = pl.last()
    while (head.element() + tail.element() != v) and (head.element() !=
            tail.element()):
        totle = head.element() + tail.element()
        if totle > v:
            tail = pl.before(tail)
        elif totle < v:
            head = pl.after(head)
    if head.element() + tail.element() == v:
        return (head, tail)
    if head.element() == tail.element():
        return None

if __name__ == '__main__':
    pl = PositionalList()
    for i in range(11):
        pl.add_last(i)
    print(pl)

    ret = find_sum_v_elements(pl, 3)
    if ret:
        first, last = ret
        print('first: {0:d}, last: {1:d}'.format(first.element(), last.element()))
    else:
        print('not found')

