# -*- coding: utf-8 -*-
# this is exercise c5.20
# the dynamic array capacity is shrink to capacity precisely that of the number
# of elements when the array goes strictly below N/2. And the array expand to
# double capacity size when it is full. Consider the following circumstances.
# let n = 2m, and we append m times first and the array is full, like m is 16,
# and then we append one time, then pop one time, oscillate between append and
# pop like the below table.
# The method field `a` means "append", repectively, `p` means "pop".
#   Nth     method      time
#   1       a           1
#   1       a           1
#   ...
#   1       a           1
#   ------------------------ m times, and array is full
#   1       a           m + 1
#   1       p           m + 1
#   1       a           m + 1
#   1       p           m + 1
#   ------------------------ m times
# So, we perform n=2m operations, and the total time is T(n) = m + m(m + 1) = m^2 + 2m
# T(n) = n^2/4 + n > n^2/4 ~ Ω(n^2)
