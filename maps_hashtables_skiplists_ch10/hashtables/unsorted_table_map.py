# -*- coding: utf-8 -*-
from map_base import MapBase

class UnsortedTableMap(MapBase):
    """ Map implementation using an unsorted table."""

    def __init__(self):
        """ Create an empty map."""
        self._table = []

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
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """ Remove Item associated with key k(raise KeyError if not found)."""
        found = False
        for j in range(len(self._table)):
            if self._table[j]._key == k:
                found = True
                break
        if found:
            self._table.pop(j)
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

