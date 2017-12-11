# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.euler_tour import EulerTour
from trees.mutable_linked_binary_tree import construct_tree

class BalanceFactorTour(EulerTour):
    """ Calculate the balance factor throught euler tour."""

    def _hook_postvisit(self, p, d, path, result):
        if not result:  # leaf
            return 0
        else:
            # proper tree node must have two children
            bf = result[1] - result[0]
            print('e: {0:s}, bf: {1:d}'.format(str(p.element()), bf))
            return max(result) + 1

if __name__ == '__main__':
     t = construct_tree('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))')
     tour = BalanceFactorTour(t)
     tour.execute()

