# -*- coding: utf-8 -*-
# Use two adaptable priority queue, one is max-oriented, the other one is
# min-oriented. And we need a dict to store each player's two locators.
#
# We add player (richard, $60) to the two priority queue respectively, and we
# get two locator: locator_max_heap for locator in max-oriented heap and
# locator_min_heap for locator in min-oriented heap, then we add 'richard':
# (locator_max_heap, locator_min_heap) to the dict. And do the same to all
# players.
#
# In each turn, we get the max money player from the max-oriented heap,
# decrease his/her money and get the name of the player, then use the dict with
# player name to find the locator_min_heap_richard. for now, don't do any
# operation with the locator_min_heap. We get the min money player from the
# min-oriented heap, increase his/her money and get the name of the player,
# then use the dict with player name to find the locator_max_heap_solin. Then
# decrease locator_min_heap_richard and increase locator_max_heap_solin
# repectively. The procedure is like the following:
#   dec locator_max_heap_richard --> inc locator_min_heap_solin -->
#   inc locator_max_heap_solin --> dec locator_min_heap_richard

