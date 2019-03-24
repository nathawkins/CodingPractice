'''
It can be seen that the number, 125874, and its double, 251748, 
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, 
contain the same digits.
'''
import sys

def sameDigits(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)
    return str_num2.strip(str_num1) == ""

def all(values):
    return not False in values


x = 1
while True and x <= int(sys.argv[1]):
    nums = [x*i for i in range(1,7)]
    verify = [sameDigits(x,j) for j in nums]
    if all(verify):
        print(x)
        print(nums, verify)
        break
    x+=1