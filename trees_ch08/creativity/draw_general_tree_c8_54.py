# -*- coding: utf-8 -*-
# You can visit first child, then visit self, then visit all the other chilren.
# Or you can visit half children, then visit self, then visit the other half.
# or you can try some other way.
#
# Here I chose half - self -half way.
import sys
sys.path.append('../')
from trees.tree import Tree

class DrawGeneral(Tree):

    def __init__(self):
        super().__init__()
        self._count = 0

    def draw(self):
        self._draw(self.root(), 0):

    def _draw(self, p, d):
        # left half subtree
        chd = self.children(p)
        left = self.num_children(p) // 2
        idx = 0
        for c in chd:
            self._draw(c, d+1)
            idx += 1
            if idx == left:
                break
        # self
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1

        # right half subtree
        for c in chd:
            self._draw(c, d+1)

