# -*- coding: utf-8 -*-
from exception import Empty
class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []                       # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)                  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]                 # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()               # remove last item from list

def transfer(s, t):
    # pop all elements of t
    while not t.is_empty():
        t.pop()
    # pop each element of s and then push it to t
    while not s.is_empty():
        e = s.pop()
        t.push(e)

if __name__ == "__main__":
    s = ArrayStack()
    for i in range(10):
        s.push(i)
    print(s._data)
    t = ArrayStack()
    transfer(s, t)
    print(t._data)

