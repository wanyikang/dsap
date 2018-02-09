# -*- coding: utf-8 -*-
from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap

class ChainHashMap(HashMapBase):
    """ Hash map implementation with separate chaining for collision
    resolution.
    """

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(k))  # not match found
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()  # new a bucket
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if oldsize < len(self._table[j]):
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error: " + repr(k))  # not match found
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:  # only nonempty slot need be iterated
                for key in bucket:
                    yield key

if __name__ == '__main__':
    cm = ChainHashMap()
    cm['richard'] = 1
    cm['wanyikang'] = 2
    cm['rabbit'] = 3
    cm['solin'] = 4
    cm[0] = 5
    cm[1] = 6
    cm[0.1] = 7
    cm[3.14] = 'pi'
    print('cm[\'rabbit\']: {0:d}, cm[\'richard\']: {1:d}, len: {2:d}'.format(
        cm['rabbit'], cm['richard'], len(cm)))
    del cm['wanyikang']
    print('cm[\'3.14\']: {0:s}, len: {1:d}'.format(cm[3.14], len(cm)))

