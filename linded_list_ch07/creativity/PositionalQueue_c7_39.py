# -*- coding: utf-8 -*-
from positional_list import PositionalList
from exception import Empty

class PositionalQueue(object):
    """ A queue implementation based on positional list.

    With enqueue returning a position instance and support for a new method,
    delete(p), that removes the element associated with position p from the
    queue.
    """
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        """ Length method."""
        return len(self._data)

    def is_empty(self):
        """ check if the queue is empty or not."""
        return len(self._data) == 0

    def first(self):
        """ get the first element of the queue."""
        if self._data.is_empty():
            raise Empty('The queue is empty')
        return self._data.first().element()

    def enqueue(self, e):
        """ add an element to the end of the queue.
        :return: the Position of the element just be enqueued.
        """
        return self._data.add_last(e)

    def dequeue(self):
        """ remove the first element of the queue."""
        self._data.delete(self._data.first())

    def delete(self, p):
        """ Delete the element associated with position p."""
        self._data.delete(p)

    def __repr__(self):
        return str(self._data)

if __name__ == '__main__':
    q = PositionalQueue()
    for i in range(10):
        q.enqueue(i)
    print(q)
    print('first: {0:d}, is_empty: {1:s}, length: {2:d}'.format(q.first(),
        str(q.is_empty()), len(q)))
    for i in range(2):
        q.dequeue()
    pos = q.enqueue(88)
    print(q)
    q.delete(pos)
    print(q)

