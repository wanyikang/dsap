# -*- coding: utf-8 -*-
from favorites_list import FavoritesList

class Flist(FavoritesList):
    def reset_counts(self):
        walk = self._data.first()
        while walk is not None:
            walk.element()._count = 0
            walk = self._data.after(walk)

if __name__ == '__main__':
    fl = Flist()
    for i in range(10):
        fl.access(i)
    print(fl)
    fl.reset_counts()
    print(fl)

