# -*- coding: utf-8 -*-
# This is the exercise of r5.4
# make the __getitem__ method of DynamicArray support negtive indices

import ctypes                                      # provides low-level arrays

class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0                                    # count actual elements
        self._capacity = 1                             # default array capacity
        self._A = self._make_array(self._capacity)     # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not (-1 * self._n) <= k < self._n:
            raise IndexError('invalid index')
        if k < 0:
            k += self._n
        return self._A[k]                              # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:                  # not enough room
            self._resize(2 * self._capacity)             # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                            # nonpublic utitity
        """Resize internal array to capacity c."""
        B = self._make_array(c)                        # new (bigger) array
        for k in range(self._n):                       # for each existing value
            B[k] = self._A[k]
        self._A = B                                    # use the bigger array
        self._capacity = c

    def _resize_with_shifting(self, c, k):
        """ Resize internal array to capacity c and shift the elements that
        after index k rightward one element.
        """
        B = self._make_array(c)
        for i in range(k):
            B[i] = self._A[i]
        for i in range(k, self._n, 1):
            B[i + 1] = self._A[i]
        self._A = B
        self._capacity = c

    def _make_array(self, c):                        # nonpublic utitity
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()               # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:
            # not enough room, so double capacity
            self._resize_with_shifting(2 * self._capacity, k)
        else:
            # enough room, so rightward one element
            for i in range(self._n, k, -1):
                self._A[i] = self._A[i-1]
        self._A[k] = value  # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:              # found a match!
                for j in range(k, self._n - 1):    # shift others to fill gap
                    self._A[j] = self._A[j+1]
            self._A[self._n - 1] = None        # help garbage collection
            self._n -= 1                       # we have one less item
            return                             # exit immediately
        raise ValueError('value not found')    # only reached if no match


if __name__ == "__main__":
    da = DynamicArray()
    for i in range(30):
        da.append(i)
    print("da[0]:{0}; da[29]:{1}; da[-1]:{2}; da[-30]:{3}".format(
        da[0], da[29], da[-1], da[-30]))

    for i in range(10):
        da.insert(i, i + 30)
    print('len:{0}; da:[{1}]'.format(len(da), ', '.join(map(str, da))))

