# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.mutable_linked_binary_tree import MutableLinkedBinaryTree
from trees.mutable_linked_binary_tree import construct_tree
from trees.euler_tour import EulerTour


class IndentedParentheticTour(EulerTour):

    def _hook_previsit(self, p, d, path):
        space = d * '    '
        if not self.tree().is_leaf(p):
            s = space + str(p.element()) + ' (\n'
        else:
            s = space + str(p.element())
        print(s)

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            space = d * '    '
            s = space + ')\n'
            print(s)


if __name__ == '__main__':
    t = construct_tree('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))')
    tour = IndentedParentheticTour(t)
    tour.execute()

