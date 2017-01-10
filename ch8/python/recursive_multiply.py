#!/usr/bin/env python
'''
Author: Ping Guo
Email: TODO
Problem Statement:
    Write a recursive function to multiply two positive integers without using
    the multiply operator. You can use addition, subtraction, and bit shifting,
    but you should minimize the number of those operations.
Complexity: TODO
Usage: recursive_multiply <int1> <int2>
'''


def answer(m, n):
    '''
    if smallerInt is even, biggerInt * smallerInt = 2*(biggerInt*smallerInt/2)
    if smallerInt is odd, biggerInt * smallerInt = 2*(biggerInt*smallerInt/2)+biggerInt
    '''
    def recursiveMultiply(smallerInt, biggerInt):
        if smallerInt == 0:
            return 0
        elif smallerInt == 1:
            return biggerInt
        else:
            halfSmaller = smallerInt >> 1
            halfProduct = recursiveMultiply(halfSmaller, biggerInt)
            if smallerInt % 2 == 0:
                productFinal = halfProduct + halfProduct  # cannot use shift operator for recursion
            else:
                productFinal = halfProduct + halfProduct + biggerInt
            return productFinal

    if m <= n:
        smaller = m
        bigger = n
    else:
        smaller = n
        bigger = m

    return recursiveMultiply(smaller, bigger)




# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    args = docopt(__doc__)
    m = int(args['<int1>'])
    n = int(args['<int2>'])

    print answer(m, n)
