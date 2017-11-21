# -*- coding: utf-8 -*-
# Let's say we use a doubly linked list to store 2n elements. Travese the list
# for n elements and then cut the list to doubly linked list. For now, it takes
# O(n) time. Then we iterate the former two doubly linked list at the same
# time because they are in the same length. We get the first element of two
# list, add them to a new empty doubly linked list, then we get the second
# element of both list, add them to the new list too until we finish the
# iteration, this takes O(n) time. So the whole algorithm takes O(n) time.

