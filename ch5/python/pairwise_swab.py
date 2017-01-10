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
Usage: pairwise_swab <int>
'''

def answer(n):
    '''
    Function to return flipped integer bits.
    '''
    # generate bitmasks

    evenmask = int(''.join([str(i % 2) for i in range(64)]), 2)
    oddmask = int(‘’.join([str(i % 2) for i in range(1, 65)]), 2)

    # extract odd and even bits
    evenbits = n & evenmask
    oddbits = n & oddmask

    # combine bits for flipping odd/even
    flippedbits = (evenbits << 1) | (oddbits >> 1)

    # exit
    return flippedbits


# executable
if __name__ == '__main__':
    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)
    n = int(args['<int>'])


    # run
    print answer(m)
