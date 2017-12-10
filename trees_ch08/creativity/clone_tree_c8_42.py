# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.linked_binary_tree import LinkedBinaryTree

class BinaryTree(LinkedBinaryTree):

    def clone(self):
        t = BinaryTree()
        tr = t._add_root(self.root().element())
        self._clone(self.root(), t, tr)
        return t

    def _clone(self, p, t, tp):
        """ Clone a tree that is as same as self with inner _add_left and
        _add_right methods."""
        # add left subtree
        left = self.left(p)
        if left is not None:
            lp = t._add_left(tp, left.element())
            self._clone(left, t, lp)

        # add right subtree
        right = self.right(p)
        if right is not None:
            rp = t._add_right(tp, self.right(p).element())
            self._clone(right, t, rp)

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

