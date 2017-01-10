#!/usr/bin/env python

'''
Author: Ping Guo
Email: TODO
Problem Statement:
    Write a function that adds two numbers. You should not use + or any
    arithmetic operators.
Complexity: TODO
Usage: add_without_plus <int1> <int2>
'''


def add(x, y):
    '''
    example: 983 + 818, add two numbers without carry: 791,only carry: 1010,
                    sum = 1010 + 791, add without carry: 1701, only carry: 100
                                      sum = 1701 + 100 = 1801
    in baniry, carry = x & y << 1 (at the same digit, both are 1)
               sum without carry = x ^ y (at the same digit, only one is 1)
    '''
    if y == 0:
        return x
    sum_add = x ^ y
    carry = (x & y) << 1
    return add(sum_add, carry)


def answer(m, n):
    return add(m, n)


# executable
if __name__ == '__main__':
    # executalbe import only
    from docopt import docopt
    # check CLA
    args = docopt(__doc__)
    m = int(args['<int1>'])
    n = int(args['<int2>'])

    # run
    print answer(m, n)
