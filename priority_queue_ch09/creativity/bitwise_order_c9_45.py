# -*- coding: utf-8 -*-

def lt(key, other):
    """ Compare nonnegative integer key and other base on their binary
    expansion."""
    if type(key) is not int or type(other) is not int:
        raise ValueError('Key and other must both be integer.')
    kcopy = key
    ocopy = other
    kc = oc = 0
    while kcopy != 0 or ocopy != 0:
        if kcopy & 1:
            kc += 1
        if ocopy & 1:
            oc += 1
        kcopy = kcopy >> 1
        ocopy = ocopy >> 1
    return kc < oc

if __name__ == '__main__':
    rlt = lt(8, 6)
    print(rlt)

