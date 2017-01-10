#!/usr/bin/env python

'''
Author: Ping Guo
Email: pingg104@gmail.com
Problem Statement:
    Write code to partition a linked list around a value x, such that all nodes
less than x come before all nodes greater than or equal to x. If x is
contained within the list, the values of x only need to be after the elements
less than x (see below). The partition element x can appear anywhere in the
right partition; it does not need to appear between the left and right
partition.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
Complexity: TODO
Usage: partition_2 <int>
'''

def answer()










# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # return
    print answer(int(args['<int>']))
