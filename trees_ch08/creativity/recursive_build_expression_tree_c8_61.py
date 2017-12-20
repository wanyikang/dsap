# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
from trees.expression_tree import ExpressionTree, tokenize
from trees.collections.linked_stack import LinkedStack as Stack
from trees.collections.linked_queue import LinkedQueue as Queue


def find_root_index(tokens):
    s = Stack()
    for idx in range(len(tokens)):
        if tokens[idx] != ')':
            s.push(idx)
        else:
            s.pop()
            root = s.pop()
            s.pop()
            s.pop()  # right parenthesis
            s.push(root)
    return s.pop()


def build_expression_tree(tokens):
    if len(tokens) == 1:
        t = ExpressionTree(tokens[0])
        return t
    ridx = find_root_index(tokens)
    tokens_l = tokens[1:ridx]
    tokens_r = tokens[ridx+1:-1]
    subtree_l = build_expression_tree(tokens_l)
    subtree_r = build_expression_tree(tokens_r)
    t = ExpressionTree(tokens[ridx], subtree_l, subtree_r)
    return t


if __name__ == '__main__':
    tokens = tokenize('((((3+1)x3)/((9-5)+2))-((2x(7-4))+6))')
    t = build_expression_tree(tokens)
    print(t.evaluate())

