##cite for help on solution: https://blog.dreamshire.com/project-euler-41-solution/
def is_pandigital(n, s=9):
    n=str(n)
    test1 = len(n)==s
    test2 = '1234567890'[:s].strip(n)
    return test1 and not test2

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2==0 or n%3 == 0:
        return False
    
    r = int(n**0.5)
    f = 5
    ##anything that is divsible by an even number has
    ##to also be divisible by 2 or 3, so we don't
    ##need to check those, only 2,3,5 and then every odd
    ##power up to the sqrt of the maximum
    while f <= r:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6 ##hits all of the odd powers that aren't
               ##aren't divisible by 3
    return True

'''
Use the divisibility rule:
Check the sum of digits
9+8+7+6+5+4+3+2+1+0 = 45
8+7+6+5+4+3+2+1+0 = 36
7+6+5+4+3+2+1+0 = 28
6+5+4+3+2+1+0 = 21
5+4+3+2+1+0 = 15
4+3+2+1+0 = 10
3+2+1+0 = 6
2+1+0= 3
1+0 = 1

If the sum of digits is divisible by 3 or 9
then the original digit is also divisilbe by 3
and is not prime, so
45/3 = 15 (cannot be length 9, or 10 since adding 0)
36/3 = 12 (cannot be length 8)
28/3 = 9.33 (could be length 7)
21/3 = 7 (cannot be length 6)
15/3 = 5 (cannot be length 5)
10/3 = 3.33 (could be length 4)
6/3 = 2 (cannot be length 3)
3/3 = 1 (cannot be length 2)

The largest n-pandigital prime has to be length 7
or length 8 if we include the 0 into the calculation.
'''

START = 7654321 ##largest possible value
itr = 0
while True:
    if is_prime(START) and is_pandigital(START, s = 7):
        print(itr, START)
        break
    itr += 1
    START -= 2 ##the last digit has to be odd 
