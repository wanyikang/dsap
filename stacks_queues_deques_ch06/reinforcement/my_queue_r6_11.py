# -*- coding: utf-8 -*-
from collections import deque
from exception import Empty

class MyQueue(object):
    """ A queue ADT adapt from collections.deque."""
    def __init__(self):
        super(MyQueue, self).__init__()
        self._deque = deque()

    def enqueue(self, e):
        """ add an element to the end of the queue."""
        self._deque.append(e)

    def dequeue(self):
        """ remove the first element of the queue."""
        try:
            first = self._deque.popleft()
        except IndexError:
            raise Empty("The queue is empty!")
        return first

    def first(self):
        """ get the first element of the queue."""
        try:
            first = self._deque[0]
        except IndexError:
            raise Empty("The queue is empty!")
        return first

    def is_empty(self):
        """ check if the queue is empty or not."""
        return len(self._deque) == 0

    def __len__(self):
        return len(self._deque)

if __name__ == "__main__":
    d = MyQueue()
    for i in range(10):
        d.enqueue(i)
        print(len(d))
    d.dequeue()
    print(d.first())
    print(d.is_empty())
    for i in range(9):
        d.dequeue()
    print(d.is_empty())

