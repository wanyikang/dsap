from favorites_list import FavoritesList
from positional_list import PositionalList

class FList(FavoritesList):
    def clear(self):
        self._data = PositionalList()

if __name__ == '__main__':
    fav = FList()
    for c in 'hello. this is a test of mtf':        # well, not the mtf part...
        fav.access(c)
        k = min(5, len(fav))
        print('Top {0}) {1:25} {2}'.format(k, [x for x in fav.top(k)], fav))

    fav.clear()
    print('after clear, fav: [{0:s}], len: {1:d}'.format(fav, len(fav)))

