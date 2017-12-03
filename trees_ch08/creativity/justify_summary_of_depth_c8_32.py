# -*- coding: utf-8 -*-
# Like reinforcement 8.7. The minimum external nodes is 1, The maximum external
# nodes is a proper tree, that's (n+1)/2.
# minimum: D = n-1, is O(n).
# maximum: D = k*2^k = (log(n+1)-1)*(n+1)/2
#            < (n+1)/2 * (log2n -1)    n>0
#            = (n+1)/2 * logn
#            < logn*(2n)/2    n>0
#            = nlogn
# So, D is O(nlogn)

