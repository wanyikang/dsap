# -*- coding: utf-8 -*-
from singly_linked_list import SinglyLinkedList
from exception import Empty

class LeakyStack(object):
    """ Implementation of a leaky stack based on singly linked list.

    When push is invoked with the stack at full capacity, accept the pushed
    element at the top while “leaking” the oldest element from the bottom of
    the stack to make room.
    """
    def __init__(self, maxlen):
        super(LeakyStack, self).__init__()
        self._maxlen = maxlen
        self._data = SinglyLinkedList()
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack.

        When stack is full, drop the bottom element to make room for new
        element.
        """
        self._data.add_first(e)
        if self._size < self._maxlen:
            self._size += 1
        elif self._size <= len(self._data) // 2:
            self._resize()

    def _resize(self):
        """ Delete the elements that not in the stack."""
        self._data.cut(self._size)

    def pop(self):
        """Remove and return the element from the top of the stack (i.e.,
        LIFO).
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Leaky stack is empty!')
        rlt = self._data.remove_first()
        self._size -= 1
        return rlt

    def top(self):
        """ Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Leaky stack is empty!')
        return self._data.head()

if __name__ == '__main__':
    s = LeakyStack(20)
    for i in range(25):
        s.push(i)
    print('len: {0:d}, top: {1:d}, s: [{2:s}]'.format(len(s), s.top(), str(s._data)))
    s.push(20)
    print('len: {0:d}, top: {1:d}, s: [{2:s}]'.format(len(s), s.top(), str(s._data)))
    for i in range(19):
        s.pop()
    print('len: {0:d}, top: {1:d}, s: [{2:s}]'.format(len(s), s.top(), str(s._data)))

