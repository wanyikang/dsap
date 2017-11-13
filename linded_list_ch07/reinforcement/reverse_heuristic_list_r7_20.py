# -*- coding: utf-8 -*-
from favorites_list_mtf import FavoritesListMTF

if __name__ == '__main__':
    mtf = FavoritesListMTF()
    for i in 'abcdefg':
        mtf.access(i)
    print(mtf)

    for i in 'abcdefg'[::-1]:
        mtf.access(i)
    print(mtf)

