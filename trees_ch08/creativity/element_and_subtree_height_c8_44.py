# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.mutable_linked_binary_tree import MutableLinkedBinaryTree, construct_tree

class BinaryTree(MutableLinkedBinaryTree):

    def subtree_height(self):
        self._subtree_height(self.root())

    def _subtree_height(self, p):
        """ Print all the subtree height of tree rooted at Position p."""
        # get element of p
        s = ''
        s += str(p.element()) + ', '

        # get left subtree height
        if self.left(p) is not None:
            lh = self._subtree_height(self.left(p))
        else:
            lh = None

        # get right subtree height
        if self.right(p) is not None:
            rh = self._subtree_height(self.right(p))
        else:
            rh = None

        # print all info
        s += str(lh) + ', ' if lh is not None else ', '
        s += str(rh) + ', ' if rh is not None else ', '
        print(s)

        # return self height
        if lh is None and rh is None:
            return 0
        if lh is None: lh = 0
        if rh is None: rh = 0
        return max(lh, rh) + 1

if __name__ == '__main__':
    t = construct_tree('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))', BinaryTree)
    t.subtree_height()

