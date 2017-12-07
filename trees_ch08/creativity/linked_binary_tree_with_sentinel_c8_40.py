# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.binary_tree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """ Linked representation of a binary tree structure with sentinel
    underground.

    Within the sentinel supported  tree, we have two conventions:
    1, node must set it's left or right child to sentinel if it has no such
    child.
    2, node deleted from the tree must set it's parent to the node itself.
    """

    # nested classes
    class _Node(object):
        """ Lightweight, nopublic class for storing a node."""

        # streamline memeory usage
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """ An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """ Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """ Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """ Return True if other is a Postion representing the same
            location.
            """
            return type(other) is type(self) and other._node is self._node

    # utility methods
    def _validate(self, p):
        """ Return associated node, if position is valid."""
        if not isinstance(p, self.Position) or p._node is self._sentinel:
            raise TypeError('P must be proper Position type')
        if p._container is not self:
            raise ValueError('P does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('P is no longer valid')
        if p._node._left is None or p._node._right is None:
            raise ValueError('Invalid position p, children can not be None')
        return p._node

    def _make_position(self, node):
        """ Return Position instace for given node (or None if no node)."""
        if node is None or node is self._sentinel:
            return None
        else:
            return self.Position(self, node)

    def _uniform_sentinel(self, tree):
        """ Uniform the sentinel node to the same with self."""
        tmp = []
        for pos in tree.inorder():
            tmp.append(pos)
        for pos in tmp:
            if pos._node._left is tree._sentinel:
                pos._node._left = self._sentinel
            if pos._node._right is tree._sentinel:
                pos._node._right = self._sentinel

    # constructor
    def __init__(self):
        """ Create an initially empty binary tree."""
        self._sentinel = self._Node(None)
        # make the children to sentinel itself
        self._sentinel._right = self._sentinel._left = self._sentinel
        self._size = 0

    # public accessors
    def __len__(self):
        """ Return the total number of elements in the tree."""
        return self._size

    def __str__(self):
        """ str representation of linked binary tree."""
        s = ''
        for item in self:
            s += str(item)
        return s

    def root(self):
        """ Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._sentinel._left)

    def parent(self, p):
        """ Return the Position of p's parent (or None if p is root)."""
        node = self._validata(p)
        return self._make_position(node._parent)

    def left(self, p):
        """ Return the Position of p's left child (or None if no left
        child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """ Return the Position of p's right child (or None if no right
        child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """ Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not self._sentinel:
            count += 1
        if node._right is not self._sentinel:
            count += 1
        return count

    # nonpublic mutators
    def _add_root(self, e):
        """ Place element e at the root of an empty tree and return new
        Position. Raise ValueError if tree nonempty.
        """
        if self._sentinel._left is not self._sentinel:
            raise ValueError('Root exists')
        self._size = 1
        self._sentinel._left = self._Node(e, self._sentinel, self._sentinel,
                self._sentinel)
        return self._make_position(self._sentinel._left)

    def _add_left(self, p, e):
        """ Create a new left child for Position p, storing element e.

        :return: the Position of new node.
        :raise: ValueError if Position p is invalid or p already has a left
        child.
        """
        node = self._validate(p)
        if node._left is not self._sentinel:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node, self._sentinel, self._sentinel)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """ Create a new right child for Position p, storing element e.

        :return: the Position of new node.
        :raise: ValueError if Position p is invalid or p already has a right
        child.
        """
        node = self._validate(p)
        if node._right is not self._sentinel:
            raise ValueError('Left child exists')
        self._size += 1
        node._right = self._Node(e, node, self._sentinel, self._sentinel)
        return self._make_position(node._right)

    def _delete(p):
        """ Delete the node at Position p, and replace it with its child, if
        any.
        :return : the element that had been stored at Position p.
        :raise : ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left is not self._sentinel else node._right
        child._parent = node._parent
        if node._parent._left is node:
            node._parent._left = child
        else:
            node._parent._right = child
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        """ Attach trees t1 and t2, respectively, as the left and right
        subtrees of the external Position p. As a side effect, set t1 and t2 to
        empty.

        :raise : TypeError if trees t1 and t2 do not match type of this tree.
        :raise : ValueError if Position p is invalid or not external.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        # attach t1
        if not t1.is_empty():
            # uniform the sentinel instance
            self._uniform_sentinel(t1)
            # attach
            node._left = t1._sentinel._left
            t1._sentinel._left._parent = node
            # set t1 to empty
            t1._sentinel._left = t1._sentinel
            t1._size = 0
        # attach t2
        if not t2.is_empty():
            # uniform the sentinel instance
            self._uniform_sentinel(t2)
            # attach
            node._right = t2._sentinel._left
            t2._sentinel._left._parent = node
            # set t2 to empty
            t2._sentinel._left = t2._sentinel
            t2._size = 0
        return


if __name__ == '__main__':
    t = LinkedBinaryTree()
    rt = t._add_root(0)
    l = t._add_left(rt, 1)
    r = t._add_right(rt, 2)
    print('t: {0:s}'.format(t))
    print('len: {0}, left: {1}, right:{2}, root: {3}'.format(len(t),
        t.left(rt).element(), t.right(rt).element(), t.root().element()))

    t1 = LinkedBinaryTree()
    root = t1._add_root(3)
    left = t1._add_left(root, 5)
    right = t1._add_right(root, 6)
    print('t1: {0:s}'.format(t1))

    t2 = LinkedBinaryTree()
    root = t2._add_root(4)
    left = t2._add_left(root, 7)
    right = t2._add_right(root, 8)
    print('t2: {0:s}'.format(t2))

    t._attach(l, t1, t2)
    print('t: {0:s}'.format(t))

    t3 = LinkedBinaryTree()
    root = t3._add_root(9)
    left = t3._add_left(root, 'a')
    right = t3._add_right(root, 'b')
    l = t.left(t.left(t.left(t.root())))
    t._attach(l, t1, t3)
    print('t: {0:s}'.format(t))
    rt = t.root()
    print('len: {0}, left: {1}, right:{2}, root: {3}'.format(len(t),
        t.left(rt).element(), t.right(rt).element(), t.root().element()))

