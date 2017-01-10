#!/usr/bin/env python

'''
Author: Ping Guo
Email: pingg104@gmail.com
Problem Statement:
    Given an infinite number of quarters (25 cents), dimes (10 cents), nickels
(5 cents), and pennies (1 cent), write code to calculate the number of ways of
representing N cents.
Complexity: TODO
Usage: conversion <int>
'''

def answer(n):

    def makechange(amount, cointypes, index):
        '''
        recursive calculation:
        makechange(100) = makechange(100, 0q) --- = makechange(100, 0q, 0d) --- = makechange(100, 0q, 0d, 0n)
                          +                         +                             +
                          makechange(100, 1q)       makechange(100, 0q, 1d)       makechange(100, 0q, 0d, 1n)
                          +                         +                             +
                          ...                       ...                           ...
                          makechange(100, 4q)       makechange(100, 0q, 10d)      makechange(100, 0q, 0d, 20n)
        '''
        # reach to penny, which is the bottom
        if index >= len(cointypes) - 1:
            return 1
        cointype = 0
        cointype = cointypes[index]
        ways = 0
        amountRemain = 0
        i = 0
        while i*cointype <= amount:
            amountRemain = amount - i * cointype
            i += 1
            ways += makechange(amountRemain, cointypes, index+1)

        return ways
    # calculate ways of change based cointypes
    cointypes = [25, 10, 5, 1]
    return makechange(n, cointypes, 0)


# executable
if __name__ == '__main__':
    # executable import only
    from docopt import docopt
    # check CLA
    args = docopt(__doc__)
    n = int(args['<int>'])
    print answer(n)
