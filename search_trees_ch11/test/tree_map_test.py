# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from search_trees.tree_map import TreeMap
from random import shuffle

if __name__ == '__main__':
    smap = TreeMap()
    l = [i for i in range(200000)]
    shuffle(l)
    print('after shuffle!')
    for i in l:
        smap[i] = 'v_' + str(i)  # __setitem__
    print('after constructing the binary search tree!')

    # __getitem__
    print('smap[0]:{0}, smap[1]:{1}, smap[19]:{2}'.format(smap[0], smap[1],
        smap[19]))

    # first, last, before, after
    first = smap.first()
    last = smap.last()
    afrt = smap.after(first)
    blst = smap.before(last)
    print('first:{0}, after first:{1}, last:{2}, before last:{3}'.format(
        first.key(), afrt.key(), last.key(), blst.key()))

    # find_position
    print('find_position(110): {0}'.format(smap.find_position(110).key()))

    # find_ge
    print('find_ge(99): {0}'.format(smap.find_ge(99)))

    # find_range
    for item in smap.find_range(None, 10):
        print(item)

    # __iter__
    cnt = 0
    for item in smap:
        print item
        cnt += 1
        if cnt == 10:
            break

    # delete
    del smap[163467]
    try:
        smap[163467]
    except KeyError:
        print('del key correct!')

