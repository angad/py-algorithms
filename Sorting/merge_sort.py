#!/usr/bin/env python
# encoding: utf-8
"""
merge_sort.py

Created by Angad Singh on 2011-03-31.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""

import sys
import os

def merge_sort(A):
	n = len(A)
	if n==1 : return A
	mid = n//2
	L = merge_sort(A[mid:])
	R = merge_sort(A[:mid])
	return merge(L,R)

def merge(L,R):
	i = 0
	j = 0
    answer = []
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            answer.append(L[i])
            i += 1
        else:
            answer.append(R[j])
            j += 1
    if i<len(L):
        answer.extend(L[i:])
    if j<len(R):
        answer.extend(R[j:])
    return answer

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
	main()

