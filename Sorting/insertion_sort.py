#!/usr/bin/env python
# encoding: utf-8
"""
insertion_sort.py

Created by Angad Singh on 2011-03-31.
"""

import sys
import os

def insertion_sort(A):
	"""
	Input: List A with numbers
	Output: Sorted list using in-place insertion sort
	"""
	for i in range(len(A)):
		value = A[i]
		j = i-1
		while j>-1 and A[j] > value:
				A[j+1] = A[j]
				j = j-1
		A[j+1] = value
	return A	

def read_file(filename):
	"""
	Input: filename
	Returns: List L with file lines
	"""
	try:
		fp = open(filename)
		L = fp.readlines()
	except IOError:
		print "Error opening or reading the file: ", filename
		sys.exit()
	return L

def main():
	if len(sys.argv) != 2:
		print "Usage: insertion_sort.py filename"
	else:
		filename = sys.argv[1]
		numbers = read_file(filename)
		sorted_numbers = insertion_sort(numbers)
		print sorted_numbers

if __name__ == '__main__':
 	import profile
    profile.run("main()")

