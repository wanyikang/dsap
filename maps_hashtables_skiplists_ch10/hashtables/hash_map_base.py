# -*- coding: utf-8 -*-
from map_base import MapBase
from random import randrange

class HashMapBase(MapBase):
    """ Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """ Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        mad = (hash(k) * self._scale + self._shift) % self._prime
        return mad % len(self._table)

    def __len__(self):
        return self._n

    def _bucket_getitem(self, j, k):
        """ Search the bucket referenced by j with key k.

        raise KeyError if not found.
        """
        raise NotImplemented

    def _bucket_setitem(self, j, k, v):
        """ Modify bucket referenced by j so that key k becomes associated with
        value v.

        Note: when a new item is inserted, this method is responsible for
        incrementing self._n.
        """
        raise NotImplemented

    def _bucket_delitem(self, j, k):
        """ Remove the item having key k from the bucket referenced by j.

        raise KeyError if not found.
        """
        raise NotImplemented

    def __iter__(self):
        raise NotImplemented

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:  # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)  # 2*x-1 if often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):
        """ Resize bucket array to capacity c. It will rehash the hash table
        and the bucket array index of one item may change."""
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for k,v in old:
            self[k] = v  # reinsert old key-value pair

