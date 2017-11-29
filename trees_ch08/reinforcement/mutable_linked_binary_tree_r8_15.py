# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.linked_binary_tree import LinkedBinaryTree

class MutableLinkedBinaryTree(LinkedBinaryTree):

    def add_root(self, e):
        return self._add_root(e)

    def add_left(self, p, e):
        return self._add_left(p, e)

    def add_right(self, p, e):
        return self._add_right(p, e)

    def replace(self, p, e):
        return self._replace(p, e)

    def delete(self, p):
        return self._delete(p)

    def attach(self, p, t1, t2):
        self._attach(p, t1, t2)

if __name__ == '__main__':
    t = MutableLinkedBinaryTree()
    root = t.add_root(0)
    l = t.add_left(root, 1)
    r = t.add_right(root, 2)

    t1 = MutableLinkedBinaryTree()
    root = t1.add_root(3)
    left = t1.add_left(root, 5)
    right = t1.add_right(root, 6)

    t2 = MutableLinkedBinaryTree()
    root = t2.add_root(4)
    left = t2.add_left(root, 7)
    right = t2.add_right(root, 8)

    t.attach(l, t1, t2)

    for item in t:
        print(item)

