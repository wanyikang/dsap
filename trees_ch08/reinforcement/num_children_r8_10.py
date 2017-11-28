# -*- coding: utf-8 -*-
from tree import Tree

class BinaryTree(Tree):
    """ Abstract base class representing a binary tree structure."""

    # abstract methods
    def left(self, p):
        """ Return a Position representing p's left child.

        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """ Return a Position representing p's right child.

        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclass')

    # concrete methods
    def sibling(self, p):
        """ Return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None  # p must be root, root has no sibling
        else:
            if self.left(parent) == p:
                return self.right(parent) # possibly None
            else:
                return self.left(parent)  # possibly None

    def children(self, p):
        """ Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def num_children(self, p):
        """ Return the number of children that Position p has."""
        cnt = 0
        if self.left(p) is not None:
            cnt += 1
        if self.right(p) is not None:
            cnt += 1
        return cnt

    def inorder(self):
        """ Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """ Generate an inorder iteration of positions in subtree rooted at p."""
        # if child exists, traverse it's subtree
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        # visit p between it's subtrees
        yield p
        # if right child exists, traverse it's subtree
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # override inherited version to make inorder the default
    def positions(self):
        """ Generate an iteration of the tree's positions."""
        return self.inorder()  # make inorder the default

