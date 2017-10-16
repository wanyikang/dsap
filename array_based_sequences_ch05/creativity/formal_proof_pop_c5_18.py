# -*- coding: utf-8 -*-
# this is exercise c5.18
# the prove for append is the same to c5.15, please check it out.
# Following is the prove of pop method:
# Assume an array of length n, we pop it to lower than n/4, then it will be
# shrink to n/2, so the amortized time for each pop is:
# ⎣ n/2⎦ / ⎡ 3n/4⎤ <= (n/2) / ⎡ 3n/4⎤ <= (n/2) * (4/3n) = 2/3 < 1
# so we can add 1 unit time to each pop operation to amortize the shrink.
