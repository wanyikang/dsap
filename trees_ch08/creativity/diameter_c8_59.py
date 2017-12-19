# -*- coding: utf-8 -*-
# Before we solve the problem, we must do two proves.
# 1, the diameter position p and q are both leaf nodes of tree T.
# 2, one of the diameter position p and q is the maximum depth leaf.
#
# Prove 1:
# Assume one of the diameter position is not a leaf, let's say p is not a leaf.
# So (dp + dq - 2da) is maximum. But, p is not a leaf, so p at leat has one
# child, assume p', so obviously (dp' + dq -2da) > (dp + dq - 2da), That's
# impossble, because the (dp + dq - 2da) is maximum. So we know both of them
# are leaf.
#
# Prove 2:
# Assume there is a diameter position p and q that both of them are not the
# maximum depth leaf. So we get (dp + dq - 2da) too. So assume the maximum
# depth node exist at the sibling of lca node, Then we get that we can find
# another diameter position pair include the maximum depth node. Assume the
# maximum depth node exist at the lca subtree. We can also find another
# diameter position pair include maximum depth. So we know one of the diameter
# positon is the maximum depth leaf.
#
# Algorithm diameter(t):
#   traverse tree t and save the depth of all nodes to the nodeself and append
#   all leaf node to a list ll
#   sort(ll) by depth increasing
#   max_leaf = list.pop()
#   dl = []
#   for item in reverse_list:
#       if lca(max_leaf, item) == t.root():
#           return calculate_diameter(max_leaf + item)
#       else:
#           dl.append(calculate_diameter(max_leaf + item))
#   return max(dl)
#
# The running time is O(Dmax*Cleaf + N). Dmax means depth of maximum depth
# node, Cleaf means count of all leaf of tree t, N means number of all nodes.

