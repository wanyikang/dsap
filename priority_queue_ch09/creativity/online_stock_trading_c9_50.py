# -*- coding: utf-8 -*-
# We build two priority queue, one max-oriented heap for buy order and one
# min-oriented heap for sell order.
# When min element in sell heap is greater than max element in buy heap, There
# is no order to be processed, otherwise, remove_min in sell heap and
# remove_max in buy heap and process the two orders. And do the above procedure
# again and again.

