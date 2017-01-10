#!/usr/bin/env python

'''
Author: Ping Guo
Email: pingg104@gmail.com
Problem Statement:
    You are given two sorted arrays, A and B, where A has a large enough buffer
    at the end to hold B. Write a method to merge B into A in sorted order.
Example: A = [1, 5, 9]
    B = [2, 4, 7]
    C = [6, 9, 22, 34, 87, 98,101]
    D = [3, 6, 9, 10, 23, 68, 90, 403, 3049]
Usage:
    sorted_merge <A> <B>
    sorted_merge case1
    sorted_merge case2
'''

def answer1(a, b):
    '''
    Function for basic solution to problem
    Complexity: O(AB)
    '''
    for i, __ in enumerate(b):
        for j, __ in enumerate(a):
		    if b(i) >= a(j) and b(i) < a(j+1):
			        a.insert(j+1, b(i))
		            break

def answer2(a, b):
	'''
	Function with bookmark to record last insert to improve performance
	Complexity: O(AB)
	'''
	start = 0
	for i, __ in enumerate(b):
		for j, __ in enumerate(a[start:]):
			if b(i) >= a(j) and b(i) < a(j+1):
				a.insert(j+1, b(i))
				start = j+1
				break

def answer3(a, b):


[1,3,6,9, 22, 34, 87, 98,101]


# executable
if __name__ == '__main__':

    # exectuable import only
    from docopt import docopt

    # check CLA
    args = docopt(__doc__)

    answer(args['<A>'], args['<B>'])
