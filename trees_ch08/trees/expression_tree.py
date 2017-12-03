# -*- coding: utf-8 -*-
from linked_binary_tree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    """ An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """ Create an expression tree.

        In a single parameter form, token should be a leaf value (e.g., '42'),
        and the expression tree will have that value at an isolated node.

        In a three-parameter version, token should be an operator, and left and
        right should be existing ExpressionTree instances that become the
        operands for the binary operator.
        """
        super(ExpressionTree, self).__init__()
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token)
        if left is not None:
            if token not in '+-*x/':
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right)

    def __str__(self):
        """ Return string representation of the expression."""
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        """ Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            return result.append(str(p.element()))
        else:
            result.append('(')
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(')')

    def evaluate(self):
        """ Return the numeric result of the expression."""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())      # we assume element is numeric
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:                          # treat 'x' or '*' as multiplication
                return left_val * right_val

def tokenize(raw):
    """ Token the raw string to ignore whitespace and to recognize multidigit
    number as a single token.

    For example, '(35 + 14)' must be tokenized to list ['(', '35', '+', '14' ,
    ')']
    :param raw : the raw parenthesize str
    """
    rlt = []
    mark = 0  # mark the first char before a digit
    for i in range(len(raw)):
        if raw[i] in '( )+-*x/':
            digits = raw[mark+1:i]
            if digits:
                rlt.append(digits)
            if raw[i] != ' ':
                rlt.append(raw[i])
            mark = i
    return rlt

def build_expression_tree(tokens):
    """Returns an ExpressionTree based upon by a tokenized expression.

    tokens must be an iterable of strings representing a fully parenthesized
    binary expression, such as ['(', '43', '-', '(', '3', '*', '10', ')', ')']
    """
    S = []                                        # we use Python list as stack
    for t in tokens:
        if t in '+-x*/':                            # t is an operator symbol
            S.append(t)                               # push the operator symbol
        elif t not in '()':                         # consider t to be a literal
            S.append(ExpressionTree(t))               # push trivial tree storing value
        elif t == ')':       # compose a new tree from three constituent parts
            right = S.pop()                           # right subtree as per LIFO
            op = S.pop()                              # operator symbol
            left = S.pop()                            # left subtree
            S.append(ExpressionTree(op, left, right)) # repush tree
        # we ignore a left parenthesis
    return S.pop()

if __name__ == '__main__':
    ts = tokenize('(15 - ((((31 + 1) x3) / ((9-5)+2))-((3x(7-4))+6)))')
    big = build_expression_tree(ts)
    print('big = {0:f}'.format(big.evaluate()))

