# -*- coding: utf-8 -*-
# Actually this is a mathamatic problem. Let's prove it.
# Assume the proper tree T has k+1 levels, k is a positive integer.
# We get:
# I(T) = 1*2^1 + 2*2^2 + 3*2^3 + ... + k*2^k
# E(T) = (k+1)*2^(k+1)
#
# And let's first get the result of I(T).
# Let    S(k) = 1*2^1 + 2*2^2 + 3*2^3 + ... + k*2^k
# Then 2*S(k) =         1*2^2 + 2*2^3 + ... + (k-1)*2^k + k*2^(k+1)
# S(k) - 2S(k) = 2^1 + 2^2 + 2^3 + ... + 2^k - k*2^(k+1)
# S(k) = k*2^(k+1) - (2^1 + 2^2 + 2^3 + ... + 2^k)
# S(k) = k*2^(k+1) - 2(2^k -1)
# S(k) = (k-1)*2^(k+1) + 2
#
# So, I(T) = (k-1)*2^(k+1) + 2, E(T) = (k+1)*2^(k+1)
# So, E(T) - I(T) = (k+1)*2^(k+1) - (k-1)*2^(k+1) + 2
#                 = 2^(k+2) - 2
#
# Let get the realtionship of k and n.
# Because k+1 is the levels number of tree T, and n is the nodes number of T.
# So we get:
# n = 2^0 + 2^1 + 2^2 + ... + 2^(k+1)
# n = 2^(k+2) -1
#
# So E(T) - I(T) = 2^(k+2) - 2 = n - 1
# E(T) = I(T) + n - 1, So we get it.

