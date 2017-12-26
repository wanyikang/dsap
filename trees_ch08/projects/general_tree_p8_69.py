# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.linked_binary_tree import LinkedBinaryTree
from trees.collections.linked_queue import LinkedQueue

class Tree(object):
    """ General tree implementation adapting a binary tree."""

    # constructor
    def __init__(self):
        self._binary_tree = LinkedBinaryTree()

    # public accessor
    def root(self):
        """ Return Position representing the tree's root (or None if empty)."""
        return self._binary_tree.root()

    def parent(self, p):
        """ Return the Position of p's parent (or None if p is root)."""
        father = self._binary_tree.parent(p)
        child = p
        while self._binary_tree.right(father) is child:
            child = father
            father = self._binary_tree.parent(child)
        return father

    def num_children(self, p):
        """ Return the number of children of Position p."""
        count = 0
        if self._binary_tree.left(p):
            child = self._binary_tree.left(p)
            while child:
                count += 1
                child = self._binary_tree.right(child)
        return count

    def children(self, p):
        """ Generate an iteration of Positions representing p's children."""
        if self._binary_tree.left(p):
            child = self._binary_tree.left(p)
            while child:
                yield child
                child = self._binary_tree.right(child)

    def __len__(self):
        """ Return the total number of elements in the tree."""
        return len(self._binary_tree)

    def __str__(self):
        """ str representation of linked binary tree."""
        s = ''
        for item in self:
            s += str(item)
        return s

    def is_root(self, p):
        """ Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """ Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """ Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """ Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        elif self._binary_tree.right(self.parent(p)) == p:
            return self.depth(self.parent(p))
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """ Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height(p)

    def __iter__(self):
        """ Generate an iteration of the tree's elements."""
        for p in self.positions():
            yield p.element()

    def positions(self):
        """ Generate an iteration of the tree's positions."""
        return self.preorder()  # return entire preorder iteration

    def preorder(self):
        """ Generate a preorder iteration of positions in the tree."""
        return self._binary_tree.preorder()

    def postorder(self):
        """ Generate a postorder iteration of positions in the tree."""
        return self._binary_tree.inorder()

    def breadthfirst(self):
        """ Generate a breadth-first iteration of the positions of the tree."""
        return self._binary_tree.breadthfirst()

    # nonpublic mutators
    def _add_root(self, e):
        """ Place element e at the root of an empty tree and return new
        Position. Raise ValueError if tree nonempty.
        """
        return self._binary_tree._add_root(e)

    def _add_child(self, p, e):
        """ Create a new child for Position p, storing element e."""
        left = self._binary_tree.left(p)
        if left is not None:
            return self._binary_tree._add_right(left, e)
        else:
            return self._binary_tree._add_left(p, e)

    def _replace(self, p, e):
        """ Replace the element at position p with e, and return old
        element."""
        return self._binary_tree._replace(p, e)

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if
        any.

        :return : the element that had been stored at Position p.
        :raise : ValueError if Position p is invalid or p has two children.
        """
        if self.num_children(p) > 1:
            raise ValueError('Position has more than one child')
        elif self.num_children(p) == 0:
            self._binary_tree._delete(p)
        else:
            child = self._binary_tree.left(p)._node
            if p == self.root():
                self._binary_tree._root = p._node
            else:
                parent = self.parent(p)._node
                parent._left = child
                child._parent = parent
            self._binary_tree._size -= 1
            p._node._parent = p._node
        return p.element()

    def _attach(self, p, t_list):
        """ Attach trees storing in t_list to the external Position p in the
        order with t_list itself. As a side effect, trees in t_list will be set
        to empty.

        :raise : TypeError if trees in t_list do not match type of this tree
        :raise : ValueError if Position p is invalid or not external.
        """
        if not t_list:
            return
        if self._binary_tree.left(p) is None:
            t1 = t_list.pop(0)
            if not type(self) is type(t1):
                raise TypeError('Tree types must match')
            t2 = LinkedBinaryTree()
            self._binary_tree._force_attach(p, t1._binary_tree, t2)
        left = self._binary_tree.left(p)
        for t2 in t_list:
            if type(t2) is not type(self):
                raise TypeError('Tree types must match')
            t1 = LinkedBinaryTree()
            self._binary_tree._force_attach(left, t1, t2._binary_tree)
        return

if __name__ == '__main__':
    t = Tree()
    rt = t._add_root(0)
    l = t._add_child(rt, 1)
    r = t._add_child(rt, 2)
    print('tree: {0:s}, len: {1:d}'.format(str(t), len(t)))

    t1 = Tree()
    root = t1._add_root(3)
    left = t1._add_child(root, 5)
    right = t1._add_child(root, 6)

    t2 = Tree()
    root = t2._add_root(4)
    left = t2._add_child(root, 7)
    right = t2._add_child(root, 8)

    t._attach(l, [t1, t2])
    print('tree: {0:s}, len: {1:d}'.format(str(t), len(t)))

    root = t.root()
    print('root: {}'.format(root.element()))
    c_iter = t.children(root)
    child = c_iter.next()
    c_iter = t.children(child)
    child = c_iter.next()
    child = c_iter.next()
    c_iter = t.children(child)
    child = c_iter.next()
    print('depth: {}'.format(t.depth(child)))
    print('height: {}'.format(t.height()))
    t._delete(child)
    print('tree: {0:s}, len: {1:d}'.format(str(t), len(t)))

