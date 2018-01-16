import sys
sys.path.append('..')
from favorites_list import FavoritesList
from priqueues.collections.positional_list import PositionalList
from priqueues.max_heap_priority_queue import MaxHeapPriorityQueue

class FavoritesListMTF(FavoritesList):
    """List of elements ordered with move-to-front heuristic."""

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

        # get all the element with form of (count, value)
        kvs = []
        for item in self._data:  # positional lists support iteration
            kvs.append((item._count, item._value))
        pq = MaxHeapPriorityQueue(kvs)  # bottom-up heap construction
        for j in range(k):
            k,v =  pq.remove_max()
            yield v


if __name__ == '__main__':
    fav = FavoritesListMTF()
    for c in 'hello. this is a test of mtf':
        fav.access(c)
        k = min(5, len(fav))
        print('Top {0}) {1:25} {2}'.format(k, [x for x in fav.top(k)], fav))

