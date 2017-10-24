# -*- coding: utf-8 -*-
# Suppose an initially empty queue Q has executed a total of 32 enqueue
# operations, 10 first operations, and 15 dequeue operations, 5 of which raised
# Empty errors that were caught and ignored. What is the current size of Q?
#
# Only the dequeue operation can decrease the size of queue, but both first and
# dequeue operations can raise empty errors, so we must decide which raise how
# many errors. And I get the following table:
#   first   dequeue     queue_size
#   5       0           32-15=17
#   4       1           32-15+1=18
#   3       2           32-15+2=19
#   2       3           32-15+3=20
#   1       4           32-15+4=21
#   0       5           32-15+5=22

