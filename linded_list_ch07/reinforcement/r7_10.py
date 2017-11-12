# -*- coding: utf-8 -*-
# When the positional list is empty, the L.first() method and L.last() method
# is returning None, and add_before()/add_after() method raised position error
# at this situation. So when the positional list is empty you can not add one
# element to it, so the add_first() and add_last() methods are necessary.
#
# Also, you can make add_before() and add_after() accept None as position
# parameter, and those methods add element to first or last when the position
# parameter is None. It looks weird, when I give a wrong position to a method,
# I hope it do nothing and report a error to me. So creating add_first() and
# add_last() methods is a better design decision.

