# -*- coding: utf-8 -*-
# Continued from r6.8
# Only the dequeue operation can decrease the size of queue, but both first and
# dequeue operations can raise empty errors, so we must decide which raise how
# many errors. And I get the following table:
#   raised_first   raised_deq   effective_deq  front_value
#       5               0           15              15
#       4               1           14              14
#       3               2           13              13
#       2               3           12              12
#       1               4           11              11
#       0               5           10              10

