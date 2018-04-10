# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from search_trees.tree_map import TreeMap
from random import shuffle
import time

class TMap(TreeMap):

    def _subtree_search(self, p, k):
        """ Return Positon of p's subtree having key k, or last node
        searched.
        """
        while True:
            if k == p.key():  # found match
                return p
            elif k < p.key():  # search left tree
                if self.left(p):
                    p = self.left(p)
                else:
                    return p
            else: # search right tree
                if self.right(p):
                    p = self.right(p)
                else:
                    return p


if __name__ == '__main__':
    tmap = TMap()
    l = [i for i in range(200000)]
    shuffle(l)
    print('before constructing tmap!')
    print(time.time())
    for i in l:
        tmap[i] = 'v_' + str(i)
    print('after constructing tmap!')
    print(time.time())
    print(tmap[135798])
    print(time.time())

