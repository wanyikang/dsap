# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.linked_binary_tree import LinkedBinaryTree

class BinaryTree(LinkedBinaryTree):

    def clone(self):
        return self._clone(self.root())

    def _clone(self, p):
        """ Clone a tree that is as same as self with inner attach method."""
        # get left subtree
        if self.left(p) is not None:
            left = self._clone(self.left(p))
        else:
            left = BinaryTree()

        # get right subtree
        if self.right(p) is not None:
            right = self._clone(self.right(p))
        else:
            right = BinaryTree()

        # get root
        t = BinaryTree()
        t._add_root(p.element())
        t._attach(t.root(), left, right)
        return t

if __name__ == '__main__':
    t = BinaryTree()
    rt = t._add_root(0)
    l = t._add_left(rt, 1)
    r = t._add_right(rt, 2)

    t1 = BinaryTree()
    root = t1._add_root(3)
    left = t1._add_left(root, 5)
    right = t1._add_right(root, 6)

    t2 = BinaryTree()
    root = t2._add_root(4)
    left = t2._add_left(root, 7)
    right = t2._add_right(root, 8)

    t._attach(l, t1, t2)
    print(t)

    t2 = t.clone()
    print(t2)
    ml = t2.left(t2.left(t2.left(t2.root())))
    t2._delete(ml)
    print(t2)
    print(t)

