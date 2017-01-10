#!/usr/bin/env python
'''
Problem Statement: Search in Rotated Array - 10.3 (pg 150)
	Given a sorted array of ‘N’ integers that has been rotated an unknown number
	of times, write code to find an element in the array. You may assume that
	the array was originally sorted in increasing order.
EXAMPLE:
	Input: find 5 in [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
	Output: 8 (the index of 5 in the array)
NOTE:
	Rotation was to disable binary search (other wise we do binary search
	O(lg N) and be done We know we can compare first and last element to
	know if it is sorted or rotated Find boundary of sub arrays.
	solution 1: use for loop traverse through the array until element == n,
				return index of the element.
	solution 2:
Usage:
'''


# basic solution
def answer1(n_list, n):
	for i, j in enumerate(n_list):
		if j == n:
			return i

	return None


def answer2(n_list, n):
	pass
