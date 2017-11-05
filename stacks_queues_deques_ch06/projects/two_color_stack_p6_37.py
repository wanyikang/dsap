# -*- coding: utf-8 -*-
from exception import Empty

class TwoColorStack(object):
    """ It consists of two stacks—one “red” and one “blue”—and has as its
    operations color-coded versions of the regular stack ADT operations.
    """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        super(TwoColorStack, self).__init__()
        self._data = [None] * TwoColorStack.DEFAULT_CAPACITY
        self._red_size = 0  # red front is at data[0]
        self._blue_size = 0  # blue front is at data[-1]

    def red_len(self):
        """ Return the number of red elements in the stack."""
        return self._red_size

    def blue_len(self):
        """ Return the number of blue elements in the stack."""
        return self._blue_size

    def is_red_empty(self):
        """ Return True if there is no red elements."""
        return self._red_size == 0

    def is_blue_empty(self):
        """ Return True if there is no blue elements."""
        return self._blue_size == 0

    def red_push(self, e):
        """ Add element e to the top of red stack."""
        size = self._red_size + self._blue_size
        if size == len(self._data):
            self._resize(2 * size)
        avail = 0 + self._red_size
        self._data[avail] = e
        self._red_size += 1

    def blue_push(self, e):
        """ Add element e to the top of blue stack."""
        size = self._red_size + self._blue_size
        if size == len(self._data):
            self._resize(2 * size)
        avail = -1 - self._blue_size
        self._data[avail] = e
        self._blue_size += 1

    def red_pop(self):
        """ Remove and return the element from the top of the red stack
        Raise Empty exception if the red stack is empty.
        """
        if self._red_size == 0:
            raise Empty('Red stack is empty!')
        avail = 0 + self._red_size - 1
        self._data[avail] = None
        self._red_size -= 1
        # resize the underlying array
        size = self._red_size + self._blue_size
        if size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)

    def blue_pop(self):
        """ Remove and return the element from the top of the blue stack
        Raise Empty exception if the blue stack is empty.
        """
        if self._blue_size == 0:
            raise Empty('Blue stack is empty')
        avail = -1 - self._blue_size + 1
        self._data[avail] = None
        self._blue_size -= 1
        # resize the underlying array
        size = self._red_size + self._blue_size
        if size <= len(self._data) // 4:
            self._resize(len(self._data) // 2)

    def red_top(self):
        """ Return (but do not remove) the element at the top of the red stack.
        Raise Empty exception if the red stack is empty.
        """
        if self._red_size == 0:
            raise Empty('Red stack is empty!')
        avail = 0 + self._red_size - 1
        return self._data[avail]

    def blue_top(self):
        """ Return (but do not remove) the element at the top of the blue
        stack. Raise Empty exception if the red stack is empty.
        """
        if self._blue_size == 0:
            raise Empty('Blue stack is empty!')
        avail = -1 - self._blue_size + 1
        return self._data[avail]

    def _resize(self, cap):
        """ Resize the underlying list to length `cap`."""
        old = self._data
        self._data = [None] * cap
        # copy red
        for i in range(self._red_size):
            self._data[i] = old[i]
        # copy blue
        for i in range(self._blue_size):
            self._data[-1 - i] = old[-1 - i]
        return

if __name__ == '__main__':
    s = TwoColorStack()
    for i in range(10):
        s.red_push(i)
    for i in range(10, 20):
        s.blue_push(i)
    print(s._data)
    print('red_top: {0:d}, blue_top: {1:d}'.format(s.red_top(), s.blue_top()))

    s.red_push(20)
    print(s._data)
    print('red_top: {0:d}, blue_top: {1:d}'.format(s.red_top(), s.blue_top()))

    for i in range(5):
        s.red_pop()
    for i in range(6):
        s.blue_pop()
    print(s._data)
    print('red_top: {0:d}, blue_top: {1:d}'.format(s.red_top(), s.blue_top()))
    print('red_len: {0:d}, blue_len: {1:d}'.format(s.red_len(), s.blue_len()))

