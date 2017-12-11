# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.mutable_linked_binary_tree import MutableLinkedBinaryTree
from trees.mutable_linked_binary_tree import construct_tree

class BinaryTree(MutableLinkedBinaryTree):

    def path_length(self):
        depths = []
        self._path_length(self.root(), 0, depths)
        return sum(depths)

    def _path_length(self, p, d, depths):
        """ Calculate the path length of all the positions of tree rooted at p
        in O(n) time.
        :param p : positon
        :param d : depth of position p
        :param depths : list for contain the depths
        """
        # append d
        depths.append(d)
        # recur children
        for c in self.children(p):
            self._path_length(c, d+1, depths)
        return

if __name__ == '__main__':
    t = construct_tree('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))', BinaryTree)
    print('path length: {0:d}'.format(t.path_length()))

