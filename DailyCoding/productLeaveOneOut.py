'''
Given an array of integers, return a new array such that
 each element at index i of the new array is the product 
of all the numbers in the original array except the one 
at i.

For example, if our input was [1, 2, 3, 4, 5], the expected 
output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
 the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def productWithoutI(input_list):
    prod_list = []
    for i in input_list:
        new_list = [c for c in input_list]
        new_list.remove(i)
        this_prod = 1
        for item in new_list:
            this_prod *= item
        prod_list.append(this_prod)
    return prod_list

productWithoutI([3,2,1])
productWithoutI([1, 2, 3, 4, 5])

import random as r

productWithoutI([r.randint(1,10) for x in range(10000)])
