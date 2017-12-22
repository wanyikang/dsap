# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.tree import Tree

class LinkedGeneralTree(Tree):
    """ An implementation of general tree by linked structure."""

    # nested class
    class _Node(object):
        """ Lightweight, nonpublic class for storing an element."""

        # streamline memeory usage
        __slots__ = '_element', '_parent', '_children'

        def __init__(self, element, parent=None, children=None):
            self._element = element
            self._parent = parent
            if children is None:
                self._children = []

    class Position(Tree.Position):
        """ A class representing the location of a single element."""

        def __init__(self, container, node):
            """ Constructor of Position class."""
            self._container = container
            self._node = node

        def element(self):
            """ Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """ Return True if other is a Position representing the same
            location."""
            return type(other) is type(self) and other._node is self._node

    # utility methods
    def _validate(self, p):
        """ Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """ Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # constructor
    def __init__(self):
        self._root = None
        self._size = 0

    # public accessors
    def root(self):
        """ Return Position representing the tree's root (or None if empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """ Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p):
        """ Return the number of children of Position p."""
        node = self._validate(p)
        for item in node._children:
            print item._element
        return len(node._children)

    def children(self, p):
        """ Generate an iteration of Positions representing p's children."""
        node = self._validate(p)
        for item in node._children:
            pos = self._make_position(item)
            yield pos

    def __len__(self):
        """ Return the total number of elements in the tree."""
        return self._size

    def __str__(self):
        """ str representation of linked binary tree."""
        s = ''
        for item in self:
            s += str(item)
        return s

    # nonpublic mutators
    def _add_root(self, e):
        """ Place element e at the root of an empty tree and return new
        Position. Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_child(self, p, e):
        """ Create a new child for Position p, storing element e.
        NOTE: you can child to the rightmost, because I just append the new
        child to the children list.

        :return : the Position of new node
        :raise : ValueError if Position p is invalid
        """
        node = self._validate(p)
        self._size += 1
        child = self._Node(e, parent=node)
        node._children.append(child)
        return self._make_position(child)

    def _replace(self, p, e):
        """ Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if
        any.

        :return : the element that had been stored at Position p.
        :raise : ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) > 1:
            raise ValueError('Position has more than one child')
        if node._children:
            child = node._children[0]
        else:
            child = None
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child  # child becomes root
        else:
            p_chdrn = node._parent._children
            walk = 0
            while p_chdrn[walk] is not node:
                walk += 1
            p_chdrn.pop(walk)
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._element

    def _attach(self, p, t_list):
        """ Attach trees storing in t_list to the external Position p in the
        order with t_list itself. As a side effect, trees in t_list will be set
        to empty.

        :raise : TypeError if trees in t_list do not match type of this tree
        :raise : ValueError if Position p is invalid or not external.
        """
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        for t in t_list:
            if type(t) is not type(self):
                raise TypeError('Tree types must match')
            self._size += len(t)
            t._root._parent = node
            node._children.append(t._root)
            t._root = None
            t._size = 0
        return


if __name__ == '__main__':
    t = LinkedGeneralTree()
    rt = t._add_root(0)
    l = t._add_child(rt, 1)
    r = t._add_child(rt, 2)
    print('tree: {0:s}, len: {1:d}'.format(str(t), len(t)))

    t1 = LinkedGeneralTree()
    root = t1._add_root(3)
    left = t1._add_child(root, 5)
    right = t1._add_child(root, 6)

    t2 = LinkedGeneralTree()
    root = t2._add_root(4)
    left = t2._add_child(root, 7)
    right = t2._add_child(root, 8)

    t._attach(l, [t1, t2])
    print('tree: {0:s}, len: {1:d}'.format(str(t), len(t)))

    chdrn = t.children(t.root())
    pos = next(chdrn)
    chdrn = t.children(pos)
    pos = next(chdrn)
    chdrn = t.children(pos)
    next(chdrn)
    pos = next(chdrn)
    t._replace(pos, 'a')
    print('tree: {0:s}, len: {1:d}'.format(str(t), len(t)))
    print(pos.element())

    t._delete(pos)
    print('tree: {0:s}, len: {1:d}'.format(str(t), len(t)))

