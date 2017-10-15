# -*- coding: utf-8 -*-
# this is the exercise c5.15

# when expand a dynamic array that is full, we copy the elements into an array
# with ⎡ n/4⎤ additional cells, going from capacity N to capacity N + ⎡ n/4⎤,
# what gonna happen?

# before we get the above problem solved, I just want to review the original
# double capacity way.
# I consider it another way, see the following table:
#     nth  capacity  time  time_2
#     1     1           1  1 + 0
#     2     2           2  1 + 2^0
#     3     4           3  1 + 2^1
#     4     4           1  1 + 0
#     5     8           5  1 + 2^2
#     6     8           1  1 + 0
#     7     8           1  1 + 0
#     8     8           1  1 + 0
#     9     16          9  1 + 2^3
# from time_2 field of the above table, we get the total time of appending n
# elements is:
# T(n) = n + (2^0 + 2^1 + …… + 2^k) (k = ⎡logn⎤ － 1)
# T(n) = n + 2^(k + 1) - 1
#      = n - 1 + 2^(k + 1)
#      = n - 1 + 2^(k + 1)
#      = n - 1 + 2^⎡logn⎤
#  # (1 + logn >= ⎡logn⎤ ⇒ 2^(1 + logn) >= 2^⎡logn⎤, 2n >= 2^⎡logn⎤)
#      <= n - 1 + 2n = 3n - 1
# so we get T(n) <= 3n -1, that means the total time of appending n elements is
# linear asynptotic, we get the result.

# but if we draw the table of ⎡ n/4⎤ additional capacity, we get the following:
#    nth  capacity  time  time_2
#    1      1       1       1 + 0
#    2      2       2       1 + 2^0
#    3      3       3       1 + 2^1
#    4      4       4       1 + 2^1 + 1
#    5      5       5       1 + 2^2
#    6      7       6       1 + 2^2 + 2^0
#    7      7       1       1 + 0
#    8      9       8       1 + 2^2 + 2^1 + 2^0
#    9      9       1       1 + 0
#    10     12      10      1 + 2^3 + 2^0
#    11     12      1       1 + 0
#    12     12      1       1 + 0
#    13     15      13      1 + 2^3 + 2^2
#    14     15      1       1 + 0
#    15     15      1       1 + 0
#    16     19      16      1 + 2^3 + 2^2 + 2^1 + 2^0
#    17     19      1       1 + 0
#    18     19      1       1 + 0
#    19     19      1       1 + 0
#    20     24      20      1 + 2^4 + 2^1 + 1
#    21     24      1       1 + 0
#    22     24      1       1 + 0
#    23     24      1       1 + 0
#    24     24      1       1 + 0
#    25     30      25      1 + 2^4 + 2^3
#    26     30      1       1 + 0
#    27     30      1       1 + 0
#    28     30      1       1 + 0
#    29     30      1       1 + 0
#    30     30      1       1 + 0
#    31     38      31      1 + 2^4 + 2^3 + 2^2 + 2^1
#    32     38      1       1 + 0
# there is some pattern in there too, but it's hard for me the calculate it, it's
# some kind of complicated, so we just use the amortized way to understand it.
# consider after some append the dynamic array is length n, and at this time is
# full, next appending will make the array expand to n + ⎡ n/4⎤, and appending
# continue, when the length is n + ⎡ n/4⎤, the array is gonna expand again, then
# at this time we analyse the amortization. All the n + ⎡ n/4⎤ elements will be
# copied to the new array, so it will make extra n + ⎡ n/4⎤ time consuming, and
# we amortize it to ⎡ n/4⎤ elements(not n + ⎡ n/4⎤ elements, because there is a
# amortization previous time), so we get amortized time for each element in⎡ n/4⎤
# is AT = ( n + ⎡ n/4⎤ ) / ⎡ n/4⎤
# AT = ( n + ⎡ n/4⎤ ) / ⎡ n/4⎤ = 1 + n / ⎡ n/4⎤
# because ⎡ n/4⎤ >= n / 4, so 1 / (⎡ n/4⎤) <= 4 / n
# so AT = 1 + n / ⎡ n/4⎤ <= 1 + n * (4 / n) = 5
# take look at the above table, so get a infomation that amortized time tor earch
# element when append n elements is no bigger than 5.
# so we get the conclution: T(n) = (1 + 5)n, T(n) is O(n)

