# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from mutable_linked_binary_tree_r8_15 import MutableLinkedBinaryTree as BinaryTree
from trees.collections.linked_stack import LinkedStack as Stack
from trees.euler_tour import ParenthesizeTour

def construct_tree(exp):
    """ Constuct a binary tree from arithmetic expression."""
    s = Stack()
    for c in exp:
        if c == '(':
            pass
        elif c == ')':
            right = s.pop()
            op = s.pop()
            left = s.pop()
            t = BinaryTree()
            root = t.add_root(op)
            if type(left) is not type(t):
                t1 = BinaryTree()
                t1.add_root(left)
            else:
                t1 = left
            if type(right) is not type(t):
                t2 = BinaryTree()
                t2.add_root(right)
            else:
                t2 = right
            t.attach(root, t1, t2)
            s.push(t)
        else:
            s.push(c)
    return s.top()

if __name__ == '__main__':
    t = construct_tree('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))')
    pt = ParenthesizeTour(t)
    pt.execute()

