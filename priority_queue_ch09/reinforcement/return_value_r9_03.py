# -*- coding: utf-8 -*-
# operation      return        heap
# add(5, A)                    [(5,A)]
# add(4, B)                    [(4,B), (5,A)]
# add(7, F)                    [(4,B), (5,A), (7,F)]
# add(1, D)                    [(1,D), (4,B), (7,F), (5,A)]
# remove_min     (1,D)         [(4,B), (5,A), (7,F)]
# add(3, J)                    [(3,J), (4,B), (7,F), (5,A)]
# add(6, L)                    [(3,J), (4,B), (7,F), (5,A), (6,L)]
# remove_min     (3,J)         [(4,B), (5,A), (7,F),(6,L)]
# remove_min     (4,B)         [(5,A), (6,L), (7,F)]
# add(8, G)                    [(5,A), (6,L), (7,F), (8,G)]
# remove_min     (5,A)         [(6,L), (8,G), (7,F)]
# add(2, H)                    [(2,H), (6,L), (7,F), (8,G)]
# remove_min     (2,H)         [(6,L), (8,G), (7,F)]
# remove_min     (6,L)         [(7,F), (8,G)]

