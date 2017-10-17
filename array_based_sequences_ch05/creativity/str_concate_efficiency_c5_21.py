# -*- coding: utf-8 -*-
# This is the exercise of c5.21
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

if __name__ == "__main__":
    tnum = 1
    print("{0:>20s}    {1}    {2}".format("function", "doc_len", "time"))
    try:
        for i in range(2):
            doc = gen_document(10**i * 10000)
            s = "add_concate(" + str(doc) + ")"
            t_add = timeit(stmt=s, setup="from __main__ import add_concate", number=tnum)
            print("{0:>20s}    10^{1:d}    {2:<.6f}".format("add_concate", i, t_add))

            s = "append_concate(" + str(doc) + ")"
            t_add = timeit(stmt=s, setup="from __main__ import append_concate", number=tnum)
            print("{0:>20s}    10^{1:d}    {2:<.6f}".format("append_concate", i, t_add))

            s = "list_comp_concate(" + str(doc) + ")"
            t_add = timeit(stmt=s, setup="from __main__ import list_comp_concate", number=tnum)
            print("{0:>20s}    10^{1:d}    {2:<.6f}".format("list_comp_concate", i, t_add))

            s = "gen_comp_concate(" + str(doc) + ")"
            t_add = timeit(stmt=s, setup="from __main__ import gen_comp_concate", number=tnum)
            print("{0:>20s}    10^{1:d}    {2:<.6f}".format("gen_comp_concate", i, t_add))
            print("")
    except KeyboardInterrupt:
        print("")
    except Exception as e:
        print(repr(e))
        pass

