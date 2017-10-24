# -*- coding: utf-8 -*-
# It could make the order of the element in the queue be wrong.
# Consider a queue initialized with 10 capacity, and the elements are like
# following table:
#  head
#  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
#                      |
#                      |
#                    front
# the queue order is: 5678901234
#
# A queue like that is full, and when we want to enqueue one more element to
# the it, the resize will happen. If it happens like R6.10 said, then we get
# the following table:
#  head
#  0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | t | x | x | x | x | x | x | x | x | x
#  |
#  |
# front
# the queue order is: 0123456789t
#
# See, the order of queue is changed. But if we resize use the original way, we
# get this:
#  head
#  5 | 6 | 7 | 8 | 9 | 0 | 1 | 2 | 3 | 4 | t | x | x | x | x | x | x | x | x | x
#  |
#  |
# front
# the queue order is: 5678901234t, the order is still the same

