# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.expression_tree import ExpressionTree, tokenize
from trees.expression_tree import build_expression_tree


class ETree(ExpressionTree):
    def evaluate(self, map_dict):
        return self._evaluate_recur(self.root(), map_dict)

    def _evaluate_recur(self, p, md):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            if isinstance(p.element(), str):
                return float(md[p.element()])
            else:
                return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p), md)
            right_val = self._evaluate_recur(self.right(p), md)
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:  # treat 'x' or '*' as multiplication
                return left_val * right_val

if __name__ == '__main__':
    ts = tokenize('(((a+b)*c)-(d*e))')
    big = build_expression_tree(ts, ET=ETree)
    print('big = {0:f}'.format(
        big.evaluate({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})))

