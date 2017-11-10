# -*- coding: utf-8 -*-
from circularly_linked_list import CircularlyLinkedList

def is_in_same_list(x, y):
    """ check if x and y are in the same list.
    :param x: a node reference of some circularly linked list
    :param y: a node reference of some circularly linked list too
    :return: Ture if x and y are in the same list, otherwise return False
    """
    start = x
    walk = x._next
    flag = False
    if x is y:
        flag = True
    while walk is not start:
        if walk is y:
            flag = True
            break
        walk = walk._next
    return flag

if __name__ == '__main__':
    l = CircularlyLinkedList()
    for i in range(10):
        l.add_first(i)
    x = l._tail
    y = l._tail._next._next
    print('x and y is the same list: {0:s}'.format(str(is_in_same_list(x, y))))

    l2 = CircularlyLinkedList()
    for i in range(10):
        l2.add_first(i)
    y = l2._tail._next
    print('x and y is the same list: {0:s}'.format(str(is_in_same_list(x, y))))

