#!/usr/bin/env python

'''
Author: Ping Guo
Email: pingg104@gmail.com
Problem Statement:
    write a function to determine the number of bits you would need to flip to
    convert integer A to integer B.
    Example:
    Input: 29 (or: 11101), 15 (or: 01111)
    output: 2
Complexity: TODO
Usage: conversion <int1> <int2>
'''


# function
def answer(m, n):

    count = 0
    f = m ^ n
    while f != 0:
        f = f >> 1
        count += f & 1
    return count


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)
    m = int(args['<int1>'])
    n = int(args['<int2>'])

    # run
    print answer(m, n)
