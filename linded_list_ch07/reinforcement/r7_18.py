# -*- coding: utf-8 -*-
from favorites_list_mtf import FavoritesListMTF

if __name__ == '__main__':
    fav = FavoritesListMTF()
    for c in 'abcdefacfbde':
        fav.access(c)
    print([x for x in fav.top(6)])

