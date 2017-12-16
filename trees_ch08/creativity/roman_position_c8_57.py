# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.mutable_linked_binary_tree import MutableLinkedBinaryTree
from trees.mutable_linked_binary_tree import construct_tree

class RomanPositionTree(MutableLinkedBinaryTree):
    def __init__(self):
        super(RomanPositionTree, self).__init__()
        self._special_ps = []

    def special_non_roman(self):
        self._special_non_roman(self.root())
        return self._special_ps

    def _special_non_roman(self, p):
        """ Get the special non roman position recursively."""
        # lrmn: roman position of left subtree
        # ld: descendants number of left subtree
        if self.left(p):
            lrmn, ld = self._special_non_roman(self.left(p))
        else:
            lrmn, ld = 0, 0
        if self.right(p):
            rrmn, rd = self._special_non_roman(self.right(p))
        else:
            rrmn, rd = 0, 0

        all_children_roman = (ld + rd == lrmn + rrmn)
        not_self_roman = (ld - rd > 5 or ld - rd < -5)
        if not_self_roman:
            roman = lrmn + rrmn
            if all_children_roman:
                self._special_ps.append(p)
        else:
            roman = lrmn + rrmn + 1
        descendants = ld + rd + 1
        return roman, descendants


if __name__ == '__main__':
    t = construct_tree('((((3+(4-1))x3)/2)-((3x(7-(4+5)))+6))',
            RomanPositionTree)
    rlt = t.special_non_roman()
    for pos in rlt:
        print(pos.element())

