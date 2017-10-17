# -*- coding: utf-8 -*-
# this is exercise c5.19
# the prove for append method is the same to c5.15, please check it out.
# Following is the prove of pop method:
# Assume an array of length n, we pop it to lower than n/4, then it will be
# shrink to n/4, so the amortized time for each pop is:
# ⎣ n/4⎦ / ⎡ 3n/4⎤ <= (n/4) / ⎡ 3n/4⎤ <= (n/4) * (4/3n) = 1/3 < 1
# so we can add 1 unit time to each pop operation to amortize the shrink.
