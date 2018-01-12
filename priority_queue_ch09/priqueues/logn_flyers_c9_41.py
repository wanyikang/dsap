# -*- coding: utf-8 -*-
# We can use the bottom-up contruction method to build the heap, after
# finishing building, we don't do heap-sort phase II, we directly remove_min
# logn times from the heap. So the totally time is O(n + (logn)^2).
#
# So let prove O(n + (logn)^2) is O(n).
# Let n = 2^k, so logn = k. So n + (logn)^2 = 2^k + k^2, so we gonna prove
# 2^k > k^2, for some k.
# 2^k - k^2 > 0, k > c, the what c?
# f'(2^k - k^2) = ln2 * (2^k) - 2k
# f'(ln2*(2^k) - 2k) = ln2 * ln2 *2^k -2,
# for k >=3, f'(ln2*(2^k) - 2k) always > 0, So, ln2*(2^k) - 2k is a increasing
# function when k >=3, when k = 4, ln2*(2^k) - 2k > 0, So
# 2^k - k^2 is a increasing function when k >= 4
# when k = 5, 2^k - k^2 always > 0
# So 2^k always > k^2 when k >= 5, So c=4, So we get
# O(n + (logn)^2) = O(n)

