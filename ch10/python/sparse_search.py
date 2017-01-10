#!/usr/bin/env python

'''
    Author: Ping Guo
    Email: pingg104@gmail.com
    Problem Statement:
        Given a sorted array of strings that is interspersed with emtpy strings,
    write a method to find the location of a given string.
    EXAMPLE
    Input: ball, {"at", "", "", "", "ball", "", "", "cat", "", "", "dad", "", ""}
    Output: 4
    Usage: sparse_search case1
'''


# function
def answer(string, array):
    '''
    Basic solution with for loop, complexity O(N)
    '''
    # check for string
    if string in array:
        for i, s in enumerate(array):
            if s is string:
                return i

    # exit
    return None


# advanced answer
def answer2(string, array):
    '''
    Advance solution with binary search, if element is empty, move upward till
    find non-empty string, complexity from log(N) to O(N)
    '''
    return binary_search(string, array, 0, len(array)-1)

def binary_search(s, array, first, last):
    mid = (first+last)/2

    if array[mid] == None:
        right = mid + 1
        left = mid - 1
        while True:
            if right <= last and array[right] is not None:
                mid = right
                break
            elif left >= first and array[left] is not None:
                mid = left
                break

            right += 1
            left -= 1

    if s is array[mid]:
        return mid
    elif array[mid] < s:
        binary_search(s, array, mid+1, last)
    elif array[mid] > s:
        binary_search(s, array, first, mid-1)


# executable
if __name__ == '__main__':

    # executable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    # control flow
    if args['case1']:
        string = 'bad'
        array = ['abba', '', 'back', 'bad', '', '', '', 'cat', 'dance', 'gray']

    # run
    print answer2(string, array)
