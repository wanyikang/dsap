# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.mutable_linked_binary_tree import MutableLinkedBinaryTree
from trees.mutable_linked_binary_tree import construct_tree

class BinaryTree(MutableLinkedBinaryTree):

    def depth(self):
        self._depth(self.root(), 0)

    def _depth(self, p, d):
        """ Calculate the depths of all the positions of tree rooted at p in
        O(n) time."""
        # cal root
        s = ''
        s += 'e: ' + str(p.element()) + ', '
        s += 'd: ' + str(d)
        print(s)

        # cal children
        for c in self.children(p):
            self._depth(c, d+1)
        return

if __name__ == '__main__':
    t = construct_tree('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))', BinaryTree)
    t.depth()

