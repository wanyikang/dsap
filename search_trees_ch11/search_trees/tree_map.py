# -*- coding: utf-8 -*-
from trees.linked_binary_tree import LinkedBinaryTree
from map_base import MapBase

class TreeMap(LinkedBinaryTree, MapBase):
    """ Sorted map implementation using a binary search tree."""

    # override Position class
    class Position(LinkedBinaryTree.Position):
        def key(self):
            """ Return key of map's key-value pair."""
            return self.element()._key

        def value(self):
            """ Return value of map's key-value pair."""
            return self.element()._value

    # nonpublic utilities
    def _subtree_search(self, p, k):
        """ Return Positon of p's subtree having key k, or last node searched."""
        if k == p.key():  # found match
            return p
        elif k < p.key():  # search left tree
            left = self.left(p)
            if left is not None:
                return self._subtree_search(left, k)
        else:  # search right tree
            right = self.right(p)
            if right is not None:
                return self._subtree_search(right, k)
        return p  # unsuccessful search

    def _subtree_first_position(self, p):
        """ Return Position of first item in the subtree rooted at p."""
        walk = p
        while self.left(walk):  # keep walking left
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """ Return Position of last item in the subtree rooted at p."""
        walk = p
        while self.right(walk):  # keep walking right
            walk = self.right(walk)
        return walk

    # public methods
    def first(self):
        """ Return the first Position in the tree (or None if empty)."""
        if len(self) == 0:
            return None
        else:
            return self._subtree_first_position(self.root())

    def last(self):
        """ Return the last Position in the tree (or None if empty)."""
        if len(self) == 0:
            return None
        else:
            return self._subtree_last_position(self.root())

    def before(self, p):
        """ Return the Position just before p in the natural order.

        Return None if p is the first position.
        """
        self._validate(p)
        if self.left(p):  # p has left subtree
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            parent = self.parent(walk)
            while parent:
                if self.right(parent) == walk:
                    break
                walk = parent
                parent = self.parent(walk)
            return parent

    def after(self, p):
        """ Return the Position just after p in the natural order.

        Return None if p is the last position.
        """
        self._validate(p)
        if self.right(p):  # p has right subtree
            return self._subtree_first_position(self.right(p))
        else:
            # walk upward
            walk = p
            parent = self.parent(walk)
            while parent:
                if self.left(parent) == walk:
                    break
                walk = parent
                parent = self.parent(walk)
            return parent

    def find_position(self, k):
        """ Return position with key k, or else neighbor (or None if empty)."""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)  # hook for balanced tree subclasses
            return p

    def find_min(self):
        """ Return (key,value) pair with minimum key (or None if empty)."""
        p = self.first()
        return (p.key(), p.value()) if p else None

    def find_ge(self, k):
        """ Return (key,value) pair with least key greater than or equal to k.

        Return None if there does not exist such a key.
        """
        p = self.find_position(k)
        if not p:
            return None
        elif p.key() < k:
            return self.after(p)
        else:
            return (p.key(), p.value())

    def find_range(self, start, stop):
        """ Iterate all (key,value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_ge(start)
            while p and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        """ Return value associated with key k (raise KeyError if not found)."""
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)  # hook for balanced tree subclasses
            if p.key() != k:
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """ Assign value v to key k, overwriting existing value if present."""
        if self.is_empty():
            leaf = self._add_root(self._Item(k,v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v  # replace existing item's value
                self._rebalance_access(p)  # hook for balanced tree subclasses
                return
            if k < p.key():
                leaf = self._add_left(p, self._Item(k,v))
            else:
                leaf = self._add_right(p, self._Item(k,v))
            self._rebalance_insert(leaf)  # hook for balanced tree subclasses

    def __iter__(self):
        """ Generate an iteration of all keys in the map in order."""
        p = self.first()
        while p:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """ Remove the item at given Position."""
        self._validate(p)
        if self.left(p) and self.right(p):
            rplt = self.before(p)
            self._replace(p, rplt.element())
            p = rplt
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)  # if root is deleted, parent is None

    def __delitem__(self, k):
        """ Remove item associated with key k (raise KeyError if not found)."""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)  # based on the positional version
                return
            self._rebalance_access(p)  # hook for balanced tree subclasses
        raise KeyError('Key Error: ' + repr(k))  # raise key error if not found

    def _rebalance_insert(self, p): pass
    def _rebalance_access(self, p): pass
    def _rebalance_delete(self, p): pass

