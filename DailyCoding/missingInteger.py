'''
Given an array of integers, find the first missing positive 
integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. 
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def smallestInt(input_list):
	new_l = input_list
	new_l.sort()

	i = min(new_l)
	for val in new_l:
		if val != i and all([i < x for x in new_l[i:]]):
			return i
		i += 1

	return i