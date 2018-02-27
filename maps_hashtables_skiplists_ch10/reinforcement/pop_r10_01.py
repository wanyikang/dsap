# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from map_base import MapBase

class MyMap(MapBase):
    """ For give a concrete implementation of pop method."""

    def pop(self, k, d=None):
        """ Remove the item associated with key k from the map and return its
        associated value. If k is not in the map, return the default value d (
        or raise KeyError if d is None).
        """
        try:
            ret = self[k]
        except KeyError as kerr:
            if d is not None:
                return d
            else:
                raise kerr
        del self[k]
        return ret

