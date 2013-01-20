"""
@author Angad Singh
adapted from: http://stackoverflow.com/questions/278488/puzzle-find-the-most-common-entry-in-an-array
"""
import sys

class BoyerMoore:

	def find(self, arr):
		suspect = 0
		suspicionStrength = -1
		for n in arr:
			if(n == suspect):
				suspicionStrength+=1
			else:
				suspicionStrength-=1
			if(suspicionStrength <= 0):
				suspect = n
		return suspect


def main():
	bm = BoyerMoore()
	arr = [2, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2]
	print bm.find(arr)


if __name__ == "__main__":
	import profile
	profile.run("main()")
