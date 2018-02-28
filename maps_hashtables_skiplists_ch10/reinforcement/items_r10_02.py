# -*- coding: utf-8 -*-
# If directly applied to the UnsortedTableMap, the running time is O(n^2).
import sys
sys.path.append('..')
from hashtables.map_base import MapBase

class MyMap(MapBase):
    """ For give a concrete implementation of items method."""

    def items(self):
        """ Return a set-like view of (k,v) tuples for all entries."""
        for k in self:
            yield (k, self[k])

