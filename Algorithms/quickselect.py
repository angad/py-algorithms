"""
@author Angad Singh
"""
import sys
import random
import math

class QuickSelect:

	def find(self, arr, k):
		r = int(random.uniform(0, len(arr)))
		pivot = arr[r]
		a1 = []
		a2 = []
		for i in range(0, len(arr)):
			if(arr[i] > pivot):
				a1.append(arr[i])
			elif(arr[i] < pivot):
				a2.append(arr[i])
			else:
				pass

		if(k <= len(a1)):
			# its in small elements pile
			return self.find(a1, k)
		elif(k > len(arr) - len(a2)):
			# its in big elements pile
			return self.find(a2, k-(len(arr)-len(a2)))
		else:
			# its equal to the pivot
			return pivot


def main():
	qs = QuickSelect();
	arr = [1,2,3,4,5,6,7,8]
	print qs.find(arr, 1)
	print qs.find(arr, 2)
	print qs.find(arr, 3)
	print qs.find(arr, 4)
	print qs.find(arr, 5)
	print qs.find(arr, 6)
	print qs.find(arr, 7)


if __name__ == "__main__":
	import profile
	profile.run("main()")
	# main()
