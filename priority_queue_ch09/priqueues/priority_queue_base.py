# -*- coding: utf-8 -*-

class PriorityQueueBase(object):
    """ Abstract base class for a priority queue."""

    class _Item(object):
        """ Lightweight composite to store priority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys

        def __le__(self, other):
            return self._key <= other._key  # compare items based on their keys

        def __repr__(self):
            return '({0},{1})'.format(self._key, self._value)

    def __len__(self):
        """ Return the number of items in the priority queue."""
        raise NotImplementedError('must be implemented by subclass')

    def is_empty(self,):
        """ Return Ture if the priority queue is empty."""
        return len(self) == 0

    def add(self, key, value):
        """ Add a key-value pair."""
        raise NotImplementedError('must be implemented by subclass')

    def min(self):
        """ Return but do not remove (k,v) tuple with minimum key.

        raise Empty exception if empty.
        """
        raise NotImplementedError('must be implemented by subclass')

    def remove_min(self):
        """ Remove and return (k,v) tuple with minimum key.

        raise Empty excetion if empty
        """
        raise NotImplementedError('must be implemented by subclass')

