# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.euler_tour import BinaryEulerTour, construct_num_tree

class LevelNumberTour(BinaryEulerTour):

    def _hook_invisit(self, p, d, path):
        """ Compute level number for every position in an inorder traversal."""
        t = self._tree
        ln = 0
        for item in path:
            ln = ln * 2 + item + 1
        print('element: {0}, level number: {1}'.format(p.element(), ln))

if __name__ == '__main__':
    t = construct_num_tree()
    tour = LevelNumberTour(t)
    tour.execute()

