# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from priqueues.heap_priority_queue import HeapPriorityQueue
from priqueues.max_heap_priority_queue import MaxHeapPriorityQueue

class OnlineStockTrade(object):

    def __init__(self, orders):
        """ Construct two heaps from orders.

        NOTE: the quantiry of all orders are the same for now.
        """
        self._orders = orders
        self._traded = []
        self._max_heap = MaxHeapPriorityQueue()
        self._min_heap = HeapPriorityQueue()
        self._construct_heaps()

    def _construct_heaps(self):
        """ construct the max-oriented heap for buying order and the
        min-oriented heap for selling order."""
        for (movement, price, quantity) in self._orders:
            if movement == 'buy':
                self._max_heap.add(price, quantity)
            elif movement == 'sell':
                self._min_heap.add(price, quantity)
        return

    def do_trade(self):
        """ Do the trade process."""
        buy_price, qunt = self._max_heap.max()
        sell_price, qunt = self._min_heap.min()
        while buy_price >= sell_price:
            self._max_heap.remove_max()
            self._min_heap.remove_min()
            self._traded.append(('trade', sell_price, qunt))
            if self._max_heap.is_empty() or self._min_heap.is_empty():
                break
            else:
                buy_price, qunt = self._max_heap.max()
                sell_price, qunt = self._min_heap.min()
        print('Trading Done!')
        print(self._traded)
        return

if __name__ == '__main__':
    orders = (('sell', 5.1, 100),
              ('sell', 5.2, 100),
              ('sell', 5.15, 100),
              ('sell', 5.3, 100),
              ('sell', 7.1, 100),
              ('sell', 5.25, 100),
              ('sell', 5.8, 100),
              ('sell', 5.5, 100),
              ('sell', 6.05, 100),
              ('sell', 4.99, 100),
              ('buy', 5.8, 100),
              ('buy', 6.18, 100),
              ('buy', 5.21, 100),
              ('buy', 5.13, 100),
              ('buy', 5.0, 100),
              ('buy', 7.0, 100),
              ('buy', 4.94, 100),
              ('buy', 5.33, 100),)
    stock_trade = OnlineStockTrade(orders)
    stock_trade.do_trade()

