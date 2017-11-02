# -*- coding: utf-8 -*-
from exception import Empty

class ArrayDeque(object):
    """ Deque implementation ueing a python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self, maxlen=None):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._maxlen = maxlen

    def __len__(self):
        """ Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """ Return Ture if the deque is empty."""
        return self._size == 0

    def __getitem__(self, key):
        """ Return (but do not remove) the element at the index `key` of the
        deque.
        raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        if key < 0:
            key += self._size
        avail = (self._front + key) % len(self._data)
        return self._data[avail]

    def __setitem__(self, key, value):
        """ Set the element at the index `key` of the deque to value `value`.
        raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        if key < 0:
            key += self._size
        avail = (self._front + key) % len(self._data)
        self._data[avail] = value

    def appendleft(self, e):
        """ Add an element to the front of the deque."""
        if self._maxlen and self._size == self._maxlen:
            self.pop()
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def popleft(self):
        """ Delete an element to the front of the deque.
        if the deque size is less than a quarter of underlying list capacity,
        then shrink list to half.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        rlt = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # shrink the list
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return rlt

    def append(self, e):
        """ Add an element to the back of the deque."""
        if self._maxlen and self._size == self._maxlen:
            self.popleft()
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        last = (self._front + self._size - 1) % len(self._data)
        avail = (last + 1) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def pop(self):
        """ Delete an element to the back of the deque.
        if the deque size is less than a quarter of underlying list capacity,
        then shrink list to half.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        last = (self._front + self._size - 1) % len(self._data)
        rlt = self._data[last]
        self._data[last] = None
        self._size -= 1
        # shrink the list
        if self._size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return rlt

    def clear(self):
        """ Clear all contents of deque."""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def rotate(self, k):
        """ Rotate the deque n steps to the right. If n is negative, rotate to
        the left.
        """
        if self.is_empty():
            return
        direction = 0  # 0 means right, 1 means left
        if k < 0:
            direction = 1
            k *= -1
        for i in range(k):
            if direction == 0:
                self.appendleft(self.pop())
            else:
                self.append(self.popleft())
        return

    def remove(self, e):
        """ Remove first matching element."""
        found = False
        for i in range(self._size):
            avail = (self._front + i) % len(self._data)
            if self._data[avail] == e:
                found = True
                break
        if not found:
            return
        # found, then move the elements by itering
        if i > self._size // 2:
            for i in range(i, self._size - 1, 1):
                avail = (self._front + i) % len(self._data)
                avail_next = (avail + 1) % len(self._data)
                self._data[avail] = self._data[avail_next]
            last = (self._front + self._size - 1) % len(self._data)
            self._data[last] = None  # help gc
        else:
            for i in range(i, 0, -1):
                avail = (self._front + i) % len(self._data)
                avail_pre = (avail - 1) % len(self._data)
                self._data[avail] = self._data[avail_pre]
            self._data[self._front] = None  # help gc
            self._front += 1
        self._size -= 1

    def count(self, e):
        """ Count number of matches for e"""
        count = 0
        for i in range(self._size):
            avail = (self._front + i) % len(self._data)
            if self._data[avail] == e:
                count += 1
        return count

    def _resize(self, cap):
        """ Resize to a new list of capacity `cap`."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

if __name__ == '__main__':
    d = ArrayDeque()
    for i in range(10):
        d.appendleft(i)
    for i in range(10, 20):
        d.append(i)
    print(d._data)
    print('first: {0:d}'.format(d[0]))
    print('last: {0:d}'.format(d[-1]))
    print('size: {0:d}'.format(len(d)))

    for i in range(5):
        d.popleft()
    for i in range(5):
        d.pop()
    print(d._data)
    print('first: {0:d}'.format(d[0]))
    print('last: {0:d}'.format(d[-1]))
    print('size: {0:d}'.format(len(d)))

    for i in range(20, 30):
        d.appendleft(i)
    print(d._data)
    print('first: {0:d}'.format(d[0]))
    print('last: {0:d}'.format(d[-1]))
    print('size: {0:d}'.format(len(d)))

    for i in range(15):
        d.pop()
    print(d._data)
    print('first: {0:d}'.format(d[0]))
    print('last: {0:d}'.format(d[-1]))

    for i in range(30, 50):
        d.append(i)
    print(d._data)
    print('first: {0:d}'.format(d[0]))
    print('last: {0:d}'.format(d[-1]))
    print('size: {0:d}, capacity: {1:d}'.format(len(d), len(d._data)))

    for i in range(len(d)):
        d[i] = i
    print(d._data)
    print('first: {0:d}'.format(d[0]))
    print('last: {0:d}'.format(d[-1]))

    d.rotate(3)
    print(d._data)
    print('first: {0:d}'.format(d[0]))
    print('last: {0:d}'.format(d[-1]))

    d.rotate(-3)
    print(d._data)
    print('first: {0:d}'.format(d[0]))
    print('last: {0:d}'.format(d[-1]))

    d.remove(2)
    print(d._data)
    print('first: {0:d}'.format(d[0]))
    print('last: {0:d}'.format(d[-1]))

    d.remove(22)
    print(d._data)
    print('first: {0:d}'.format(d[0]))
    print('last: {0:d}'.format(d[-1]))

    print('count 2: {0:d}'.format(d.count(2)))
    print('count 3: {0:d}'.format(d.count(3)))
    [d.append(1) for i in range(3)]
    print('count 1: {0:d}'.format(d.count(1)))

    d.clear()
    print(d._data)
    print('size: {0:d}'.format(len(d)))

    d = ArrayDeque(10)
    for i in range(13):
        d.append(i)
        print(d._data)

