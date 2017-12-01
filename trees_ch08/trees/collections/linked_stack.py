# -*- coding: utf-8 -*-
from _singly_linked_list import SinglyLinkedList

class LinkedStack(SinglyLinkedList):
    """LIFO Stack implementation using a linked list as underlying storage."""

    def push(self, e):
        """Add element e to the top of the stack."""
        self.add_first(e)

    def pop(self):
        """ Remove and return the element from the top of the stack (i.e.,
        LIFO). Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.remove_first()

    def top(self):
        """ Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.head()

if __name__ == "__main__":
    s = LinkedStack()
    for i in range(20):
        s.push(i)
    print(s)
    for i in range(18):
        s.pop()
    print(s.top())

