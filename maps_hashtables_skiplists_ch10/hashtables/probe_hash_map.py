# -*- coding: utf-8 -*-
from hash_map_base import HashMapBase

class ProbeHashMap(HashMapBase):
    """ Hash map implemented with linear probing for collision resolution."""

    _AVAIL = object()

    def _is_available(self, j):
        """ Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """ Search for key k in bucket at index j.

        Return (success, index) tuple, described as follows:
        If match was found, success is Ture and index denotes its location.
        If no match found, success is False and index denotes first available
        slot.
        """
        first_avail = None
        while True:
            # this loop will stop finally, because the load factor is no more
            # than 0.5, so there must be empty slot in the table.
            if self._is_available(j):
                if first_avail is None:
                    first_avail = j  # mark this as first avail
                if self._table[j] is None:
                    return (False, first_avail)
            elif self._table[j]._key == k:
                return (True, j)
            j = (j + 1) % len(self._table)  # keep looking (cyclically)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if found:
            self._table[s]._value = v
        else:
            self._table[s] = self._Item(k, v)
            self._n += 1

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL  # mark as vacated

    def __iter__(self):
        for j in range(len(self._table)):  # scan entire table
            if not self._is_available(j):
                yield self._table[j]._key

if __name__ == '__main__':
    pm = ProbeHashMap()
    pm['richard'] = 1
    pm['wanyikang'] = 2
    pm['rabbit'] = 3
    pm['solin'] = 4
    pm[0] = 5
    pm[1] = 6
    pm[0.1] = 7
    pm[3.14] = 'pi'
    print('pm[\'rabbit\']: {0:d}, pm[\'richard\']: {1:d}, len: {2:d}'.format(
        pm['rabbit'], pm['richard'], len(pm)))
    del pm['wanyikang']
    print('pm[\'3.14\']: {0:s}, len: {1:d}'.format(pm[3.14], len(pm)))


