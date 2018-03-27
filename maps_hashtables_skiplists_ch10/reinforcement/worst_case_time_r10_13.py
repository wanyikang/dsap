# -*- coding: utf-8 -*-
# worst-case time: O(n)
# best-case time: O(n)
# The worst-case time and best-case time of seperate chaining are both O(n).
# Because it is just the putting time, and if all n elements are hashed to the
# same index, they are then added to a unsorted table, and the additional cost
# is alse O(n).
# But the getting time is very different between worse-case and best-case. The
# worst-case getting time is O(n), the best-case getting time is still O(n).

