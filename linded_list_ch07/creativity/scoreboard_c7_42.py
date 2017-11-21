# -*- coding: utf-8 -*-
from singly_linked_list import SinglyLinkedList

class GameEntry(object):
    """ Represents one entry of a list of high scores."""

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)  # e.g., '(Bob, 98)'


class Scoreboard(object):
    """ Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """ Initialize scoreboard with given maximum capacity."""
        self._board = SinglyLinkedList()
        self._cap = capacity

    def __len__(self):
        return len(self._board)

    def __getitem__(self, k):
        """ Return entry index k."""
        if k == 0:
            return self._board.head()
        if k == len(self) - 1:
            return self._board.tail()
        if k > len(self) - 1 or k < 0:
            raise IndexError('Index is out of range')
        else:
            walk = self._board._head
            for _ in range(k):
                walk = walk._next
            return walk._element

    def add(self, entry):
        """ Consider adding entry to high scores."""
        score = entry.get_score()
        # insert first element
        if len(self) == 0:
            self._board.add_first(entry)
            return
        good = score > self._board.head().get_score() or len(self) < self._cap
        if good:
            # insert an element to self._board
            prev = walk = self._board._head
            while walk is not None:
                if walk._element.get_score() > score:
                    break
                else:
                    prev = walk
                    walk = walk._next
            prev._next = self._board._Node(entry, walk)
            self._board._size += 1
            if walk is None:
                self._board._tail = prev._next
            # make the lenght of self._board to capacity
            if len(self) > self._cap:
                self._board.remove_first()
        return

    def __repr__(self):
        """ String representation of the scoreboard."""
        s = ''
        walk = self._board._head
        while walk is not None:
            s += str(walk._element.get_score()) + ','
            walk = walk._next
        return s[:-1]


if __name__ == '__main__':
    sb = Scoreboard()
    for i in range(10):
        entry = GameEntry('richard_' + str(i), i)
        sb.add(entry)
    print('scoreboard: {0:s}, length: {1:d}'.format(sb, len(sb)))

    entry = GameEntry('richard_' + str(10), 10)
    sb.add(entry)
    print('scoreboard: {0:s}, length: {1:d}'.format(sb, len(sb)))

    entry = GameEntry('richard_' + str(3), 3)
    sb.add(entry)
    print('scoreboard: {0:s}, length: {1:d}'.format(sb, len(sb)))

    print('min: {0}, max: {1}'.format(sb[0], sb[len(sb) - 2]))

