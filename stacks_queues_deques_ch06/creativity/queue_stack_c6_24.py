# -*- coding: utf-8 -*-
# When you push an element to a queue, you dequeue the original elements and
# then enqueu it again, so you can rotate the queue by this way.
# The asyptotic complexity for method is blew:
# len: O(1)
# is_empty: O(1)
# push: O(n)
# top: O(1)
# pop: O(1)

from queue import MyQueue
from exception import Empty

class QueueStack(object):
    """ implement stack ADT based on a queue."""
    def __init__(self):
        super(QueueStack, self).__init__()
        self._q = MyQueue()

    def __len__(self):
        """ return the number of elements in the stack."""
        return len(self._q)

    def is_empty(self):
        """ return True if the stack is empty."""
        return len(self._q) == 0

    def push(self, e):
        """ add element e to the top of the stack."""
        q = self._q
        q.enqueue(e)
        for i in range(len(q) - 1):
            tmp = q.dequeue()
            q.enqueue(tmp)

    def top(self):
        """ return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._q.first()

    def pop(self):
        """ remove and return the element from the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._q.dequeue()

if __name__ == "__main__":
    s = QueueStack()
    for i in range(20):
        s.push(i)
    print('s.top(): ', s.top())
    print('_data: ', s._q._deque)
    for i in range(20):
        print(s.pop())

