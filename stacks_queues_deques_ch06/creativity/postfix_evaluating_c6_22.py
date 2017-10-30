# -*- coding: utf-8 -*-
from array_stack_c6_16 import ArrayStack
from exception import PostfixError

class Postfix(object):
    """ evaluate the postfix expression."""
    def __init__(self, ps):
        self._ps = ps

    def _is_number(self, c):
        rlt = True
        try:
            int(c)
        except ValueError:
            rlt = False
        return rlt

    def _is_operator(self, c):
        if c in ['+', '-', '*', '/']:
            return True
        else:
            return False

    def _is_whitespace(self, c):
        if c in [' ', '\n', '\b']:
            return True
        else:
            return False

    def eval(self):
        s = ArrayStack()
        for item in self._ps:
            if self._is_number(item):
                s.push(item)
            elif self._is_operator(item):
                right = s.pop()
                left = s.pop()
                whole = left + item + right
                s.push(str(eval(whole)))
            elif self._is_whitespace(item):
                pass
            else:
                raise PostfixError("Wrong postfix expression!")
        return s.pop()

if __name__ == '__main__':
    # ps = '5 2 + 8 3 - * 5 /'
    ps = '5 2 + 8 *'
    pf = Postfix(ps)
    print(pf.eval())

