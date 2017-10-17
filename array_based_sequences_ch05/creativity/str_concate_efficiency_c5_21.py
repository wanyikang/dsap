# -*- coding: utf-8 -*-
# This is the exercise of c5.21
# from the result, I get the conclusion that all the concate method is in the
# same asyptotic time. I guess my python virtual machine optimize the add
# concatenation by directly mutating the string object when there is no other
# reference to the string.
from timeit import timeit

def add_concate(document):
    letters = ''
    for c in document:
        if c.isalpha():
            letters += c
    return letters

def append_concate(document):
    temp = []
    for c in document:
        if c.isalpha():
            temp.append(c)
    letters = "".join(temp)
    return letters

def list_comp_concate(document):
    """ List comprehesion concatenation"""
    letters = ''.join([c for c in document if c.isalpha()])
    return letters

def gen_comp_concate(document):
    """ Generator comprehesion concatenation"""
    letters = ''.join([c for c in document if c.isalpha()])
    return letters

def gen_document(dlen):
    temp = []
    for i in range(dlen):
        temp.append(chr(i % 26 + 65))
    return temp

sp_base = """
from __main__ import add_concate
from __main__ import append_concate
from __main__ import list_comp_concate
from __main__ import gen_comp_concate
from __main__ import gen_document
"""

if __name__ == "__main__":
    tnum = 1
    print("{0:>20s}    {1}    {2}".format("function", "doc_len", "time"))
    try:
        for i in range(4):
            sp = sp_base + "doc = gen_document(" + str(10**i * 10000) + ")"
            t_add = timeit("add_concate(doc)", setup=sp, number=tnum)
            print("{0:>20s}    10^{1:d}    {2:<.6f}".format("add_concate", i, t_add))

            t_add = timeit("append_concate(doc)", setup=sp, number=tnum)
            print("{0:>20s}    10^{1:d}    {2:<.6f}".format("append_concate", i, t_add))

            t_add = timeit("list_comp_concate(doc)", setup=sp, number=tnum)
            print("{0:>20s}    10^{1:d}    {2:<.6f}".format("list_comp_concate", i, t_add))

            t_add = timeit("gen_comp_concate(doc)", setup=sp, number=tnum)
            print("{0:>20s}    10^{1:d}    {2:<.6f}".format("gen_comp_concate", i, t_add))
            print("")
    except KeyboardInterrupt:
        print("")
    except Exception as e:
        print(repr(e))
        pass

