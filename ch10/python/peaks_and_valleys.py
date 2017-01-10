#!/usr/bin/env python

'''
Author: Ping Guo
Email: pingg104@gmail.com
Problem Statement:
    In an array of integers, a "peak" is an element which is greater than or
equal to the adjacent integers and a "valley" is an element which is less than
or equal to the adjacent integers. FOr example, in the array[5,8,6,2,3,4,6],
[8,6] and [5,2] are valleys. Given an array of integers, sort the array into an
alternating sequence of peaks and valleys.
EXAMPLE
Input: [5,3,1,2,3]
Output: [5,1,3,2,3]
Complexity: TODO
Usage:
    peaks_and_valleys -m <input>
    peaks_and_valleys test
'''

# libraries
import random


# functions
def answer(integers):

    # sort int list
    integers.sort()

    # get length of list
    length = len(integers)

    # get left and right halves
    left, right = integers[0:length/2], integers[length/2:length-1]

    # return
    return left, right


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # control flow
    if args['test']:
        integers = random.sample(range(1, 100), random.randint(1, 10))

    else:
        integers = args['<input>']

    print answer(integers)
