# -*- coding: utf-8 -*-
# The worst-case is that p is the last visited node in that traveral type.
import sys
sys.path.append('../')
from trees.mutable_linked_binary_tree import MutableLinkedBinaryTree
from trees.mutable_linked_binary_tree import construct_tree

class BinaryTree(MutableLinkedBinaryTree):

    def _traverse_next(self, trv_type, p):
        """ Do a `trv_type` traverse and return the position after p.
        :param trv_type : traversal type, must in ['pre', 'post', 'in']
        :param p : position p
        """
        if trv_type == 'pre':
            traverse = self.preorder
        elif trv_type == 'in':
            traverse = self.inorder
        elif trv_type == 'post':
            traverse = self.postorder
        else:
            traverse = inorder

        find = False
        pre = cur = None
        for pos in traverse():
            pre = cur
            cur = pos
            if pre == p:
                find = True
                break
        if not find and cur != p:
            raise 'Invalid Position p'
        elif not find and cur == p:
            cur = None  # make cur be the return value
        return cur

    def preorder_next(self, p):
        return self._traverse_next('pre', p)

    def inorder_next(self, p):
        return self._traverse_next('in', p)

    def postorder_next(self, p):
        return self._traverse_next('post', p)

if __name__ == '__main__':
    t = construct_tree('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))', BinaryTree)
    p = t.left(t.left(t.left(t.root())))
    rlt = t.postorder_next(p)
    print(rlt.element())

