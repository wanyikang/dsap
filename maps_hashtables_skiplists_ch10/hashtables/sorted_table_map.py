from map_base import MapBase

class SortedTableMap(MapBase):
    """ Map implementation using a sorted table."""

    # nonpublic methods
    def _find_index(self, k, low, high):
        """ Return index of the leftmost item with key greater than or equal to k.

        Return high + 1 if no such item qualifies.

        That is, j will be returned such that:
            all items of slice table[low:j] have key < k
            all items of slice table[j:high] have key >= k
        """
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if self._table[mid]._key == k:
                return mid
            elif self._table[mid]._key > k:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    # public methods
    def __init__(self):
        """ Create an empty map."""
        self._table = []

    def __len__(self):
        """ Return number of items in the map."""
        return len(self._table)

    def __getitem__(self, k):
        """ Return value associated with key k (raise KeyError if not found)."""
        j = self._find_index(k, 0, len(self) - 1)
        if self._table[j]._key != k or j == len(self):
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """ Assign value v to key k, overwriting existing value if present."""
        j = self._find_index(k, 0, len(self) - 1)
        if j < len(self) and self._table[j]._key == k:
            self._table[j]._value = v  # reassign value
        else:
            self._table.insert(j, self._Item(k, v))  # add new item

    def __delitem__(self, k):
        """ Remove item associated with key k (raise KeyError)."""
        j = self._find_index(k, 0, len(self) - 1)
        if j < len(self) and self._table[j]._key == k:
            del self._table[j]
        else:
            raise KeyError('Key Error ' + repr(k))

    def __iter__(self):
        """ Generate keys of the map ordered from minimum to maximum."""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """ Generate keys of the map ordered from maximum to minimum."""
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """ Return (key, value) pair with minimum key (or None if empty)."""
        if len(self) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """ Return (key, value) pair with maximum key (or None if empty)."""
        if len(self) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """ Return (key, value) pair with least key greater than or equal to k."""
        j = self._find_index(k, 0, len(self) - 1)
        if j < len(self):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, k):
        """ Return (key, value) pair with greatest key strictly less than k."""
        j = self._find_index(k, 0, len(self) - 1)
        if j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)
        else:
            return None

    def find_gt(self, k):
        """ Return (key,value) pair with least key strictly greater than k."""
        j = self._find_index(k, 0, len(self) - 1)
        if j < len(self) and self._table[-1]._key > k:
            if self._table[j]._key == k:
                return (self._table[j+1]._key, self._table[j+1]._value)
            else:
                return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_range(self, start, stop):
        """ Iterate all (key,value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self) - 1)
        while j < len(self) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1

if __name__ == '__main__':
    stm = SortedTableMap()
    # __setitem__
    for i in range(20):
        stm[i] = 'richard' + str(i)

    # __iter__
    print('stm: {0:s}'.format(str(list(item for item in stm))))

    # __getitem__
    for i in range(5):
        print('stm[{0:d}]: {1:s}'.format(i, stm[i]))

    # __delitem__
    for i in range(10):
        del stm[i]
    print('stm: {0:s}'.format(str(list(item for item in stm))))

    # find_min
    item = stm.find_min()
    if item:
        print('min: {{{0}: {1}}}'.format(item[0], item[1]))

    # find_max
    item = stm.find_max()
    if item:
        print('max: {{{0}: {1}}}'.format(item[0], item[1]))

    # find_ge
    item = stm.find_ge(14)
    if item:
        print('ge: {{{0}: {1}}}'.format(item[0], item[1]))

    # find_gt
    item = stm.find_gt(14)
    if item:
        print('gt: {{{0}: {1}}}'.format(item[0], item[1]))

    # find_lt
    item = stm.find_lt(14)
    if item:
        print('lt: {{{0}: {1}}}'.format(item[0], item[1]))

    # find_range
    rng = []
    for item in stm.find_range(None, 18):
        rng.append(item)
    print('range: {0:s}'.format(str(list(item for item in rng))))

