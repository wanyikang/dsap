# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from hashtables.map_base import MapBase
from hashtables.positional_list import PositionalList

class UnsortedTableMap(MapBase):
    """ Map implementation using an unsorted table."""

    def __init__(self):
        """ Create an empty map."""
        self._table = PositionalList()

    def __getitem__(self, k):
        """ Return value associated with key k(raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """ Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if item._key == k:
                item._value = v
                return
        # did not find match for k
        self._table.add_last(self._Item(k, v))

    def __delitem__(self, k):
        """ Remove Item associated with key k(raise KeyError if not found)."""
        found = False
        pos = self._table.first()
        while pos:
            if pos.element()._key == k:
                found = True
                break
        if found:
            self._table.delete(pos)
        else:
            raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        """ Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key  # yield the KEY

    def items(self):
        """ Return a set-like view of (k,v) tuples for all entries."""
        for item in self._table:
            yield (item._key, item._value)

if __name__ == '__main__':
    unsort_map = UnsortedTableMap()
    for i in range(10):
        unsort_map[i] = i
    print(unsort_map[9])
    unsort_map[9] = 19
    print(unsort_map[9])
    for key, value in unsort_map.items():
        print(key, value)

