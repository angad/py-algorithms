"""
@author Angad Singh
Adapted from http://rerun.me/blog/2012/08/30/maximum-continuous-subarray-problem-kandanes-algorithm/
"""
import sys

class Kandane:

	def find(self, arr):
		cumulative_sum = 0
		actual_cumulative_sum = 0
		maximum_sum = -32768
		start_index = 0
		max_start_index = 0
		max_end_index = 0
		current_index = 0
		
		for i in arr:
			cumulative_sum += i
			if(cumulative_sum > maximum_sum):
				maximum_sum = cumulative_sum
				max_start_index = start_index
				max_end_index = current_index

			if(cumulative_sum < 0):
				start_index = current_index + 1
				actual_cumulative_sum = cumulative_sum
				cumulative_sum = 0
			current_index += 1

		print "Start Index : %d" %(max_start_index)
		print "End Index : %d" %(max_end_index)
		return maximum_sum


def main():
	k = Kandane()
	arr = [-1, 3, -5, 4, 6, -1, 2, -7, 13, -3]
	print k.find(arr)


if __name__ == "__main__":
	import profile
	profile.run("main()")
