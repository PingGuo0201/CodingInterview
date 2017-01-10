#!/usr/bin/env python
'''
    Problem: Sorted Search, No Size (10.4, P150)
    You are given an array-like data structure Listy which lacks a size method.
    It does, however, have an elementAt(i) method that returns the element at
    index i in O(1) time. If i is beyond the bounds of the data structure, it
    returns -1. (For this reason, this data structure only support positive
    int). Given a Listy which contains sorted, positive integers, find the
    index at which an element x occurs. If x occurs multiple times, you may
    return any index.

    Usage: sorted_search_nosize <int1> <int2>
'''


def answer(array, x):
    n = 1
    while True:
        if array.elementAt(n) < x or array.elementAt(n) != -1:
            n = n * 2

    return binary_search(array[0:n+1], x, array[0], array[n+1])

def binary_search(array, x, left, right):
    mid = (left+right)/2
    if array[mid] == x:
        return mid
    elif array[mid] < x:
        binary_search(array, x, mid, right)
    elif array[mid] > x:
        binary_search(array, x, left, mid)
    else:
        return 'NOT FOUND'
def generate_array(m):
    if m <= 0:
        print 'Please enter a valid int for array range!'
    a_list = range(m)
    i = 0
    if i >= len(a_list):
        return -1
    return a_list


# executable
if __name__ == '__main__':
    # executable import only
    from docopt import docopt
    # check CLA
    args = docopt(__doc__)

    array = generate_array(int(args['<int1>']))

    target = int(args['<int2>'])

    print answer(array, target)
