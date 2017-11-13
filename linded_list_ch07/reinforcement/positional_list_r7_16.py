# -*- coding: utf-8 -*-
from positional_list import PositionalList

class PList(PositionalList):

    def add_last(self, e):
        """ Use methods in the following list to implement this method:
        {is_empty, first, last, before, after, add_after, add_first}
        """
        if self.is_empty():
            self.add_first(e)
        else:
            self.add_after(self.last(), e)

    def add_before(self, p, e):
        """ Use methods in the following list to implement this method:
        {is_empty, first, last, before, after, add_after, add_first}
        """
        if self.is_empty():
            self.add_first(e)
        else:
            if self.before(p):
                self.add_after(self.before(p), e)
            else:
                self.add_first(e)

if __name__ == '__main__':
    l = PList()
    for i in range(10):
        l.add_last(i)
    for i in range(-1, -10, -1):
        l.add_before(l.first(), i)
    for item in l:
        print(item)

