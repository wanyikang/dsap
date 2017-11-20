from favorites_list import FavoritesList
from positional_list import PositionalList
from leaky_stack_c7_30 import LeakyStack


class LeakyPositionalStack(LeakyStack):

    def kinds(self):
        """ Return the number of kinds of the elements in the stack."""
        d = {}
        g = iter(self._data)
        for _ in range(len(self)):
            item = g.next()
            if item not in d:
                d[item] = None
        return len(d.keys())


class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic."""

    def __init__(self, n):
        super(FavoritesListMTF, self).__init__()
        self._leaky_stack = LeakyPositionalStack(n)

    def access(self, e):
        """ Overwrite this method."""
        super(FavoritesListMTF, self).access(e)
        self._leaky_stack.push(self._data.first().element()._value)
        ntd = len(self) - self._leaky_stack.kinds()
        if ntd > 0:
            walk = self._data.last()
            for _ in range(ntd):
                prev = self._data.before(walk)
                self._data.delete(walk)
                walk = prev

    # we override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))       # delete/reinsert

    # we override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        # we begin by making a copy of the original list
        temp = PositionalList()
        for item in self._data:              # positional lists support iteration
            temp.add_last(item)

        # we repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # we have found the element with highest count
            yield highPos.element()._value                   # report element to user
            temp.delete(highPos)                             # remove from temp list

if __name__ == '__main__':
    fav = FavoritesListMTF(10)
    for c in 'hello. this is a test of mtf':
        fav.access(c)
        k = min(5, len(fav))
        print('Top {0}) {1:25} {2}'.format(k, [x for x in fav.top(k)], fav))
    print(fav._leaky_stack._data)

