# -*- coding: utf-8 -*-
from linked_binary_tree import LinkedBinaryTree
from collections.linked_stack import LinkedStack as Stack

class MutableLinkedBinaryTree(LinkedBinaryTree):

    def add_root(self, e):
        return self._add_root(e)

    def add_left(self, p, e):
        return self._add_left(p, e)

    def add_right(self, p, e):
        return self._add_right(p, e)

    def replace(self, p, e):
        return self._replace(p, e)

    def delete(self, p):
        return self._delete(p)

    def swap(self, p, q):
        return self._swap(p, q)

    def attach(self, p, t1, t2):
        self._attach(p, t1, t2)


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
            t = MutableLinkedBinaryTree()
            root = t.add_root(op)
            if type(left) is not type(t):
                t1 = MutableLinkedBinaryTree()
                t1.add_root(left)
            else:
                t1 = left
            if type(right) is not type(t):
                t2 = MutableLinkedBinaryTree()
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
    print(t)
    # p = t.left(t.left(t.root()))
    p = t.right(t.left(t.left(t.left(t.root()))))
    print('p: {0:s}'.format(p.element()))
    # q = t.left(t.right(t.root()))
    q = t.left(t.right(t.left(t.root())))
    print('q: {0:s}'.format(q.element()))
    # t.swap(p, q)
    t.swap(q, q)
    print(t)

