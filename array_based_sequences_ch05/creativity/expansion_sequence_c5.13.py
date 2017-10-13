# -*- coding: utf-8 -*-
# this is the exercise of c5.13
# the expansion sequence will change with nonempty length, for example, let the
# initail len be 2, the sequence is the following:
# [2, 6, 10, 18, 27, 37, 48, 61, 75, 91, ...] if initial len == 2
# [0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...]  if initial len == 0

# I do some exploration, it seems that the underlining dynamic array expanding
# constant is 1.125, nor 2 or 1.5, it allocates 1.125 * new_size + 6 (or + 3
# when the array is smaller than 9 elements)
