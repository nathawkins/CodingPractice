'''
By replacing the 1st digit of the 2-digit number *3, it turns out that six of 
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, 
this 5-digit number is the first example having seven primes among the 
ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, 
and 56993. Consequently 56003, being the first member of this family, is the 
smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily 
adjacent digits) with the same digit, is part of an eight prime value family.
'''

###Using some logic from https://www.mathblog.dk/project-euler-51-eight-prime-family/

import time

def isPrime(n):
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

def get_primes(limit):
    '''Sieve of Atkin. Wrote this code for Problem 10'''
    ##Start with the formation of an array that holds the prime numbers
    P = [2,3]

    ##Make an array of Boolean's, all False to begin with, of length limit
    sieve=[False]*(limit+1)

    ##Now do the sifting, checking x values up until the sqrt(limit)
    for x in range(1,int((limit)**(1/2))+1):

        ##y values cover the same limits
        for y in range(1,int((limit)**(1/2))+1):

            '''
            All numbers with modulo-sixty remainder 1, 13, 17, 29, 37, 41, 49, or 53 have a modulo-twelve remainder of 1 or 5.
            '''
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5): ##If the value of n is divisible by 12 and has remainder 1 and 5
                sieve[n] = not sieve[n]           ##then flip the value of that entry in the sieve array.


            '''
            All numbers with modulo-sixty remainder 7, 19, 31, or 43 have a modulo-six remainder of 1.
            '''
            n = 3*x**2+y**2
            if n<= limit and n%12==7:             ##If the value of n is divisible by 12 and has a remainder of 7
                sieve[n] = not sieve[n]           ##then flip that value


            '''
            n needs to be a positive solution, so we have to check and make sure x is greater than y. All numbers with modulo-sixty remainder 11, 23, 47, or 59 have a modulo-twelve remainder of 11.
            '''
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11:     ##If the value of n is divisible by 12 and has a remainder 11
                sieve[n] = not sieve[n]           ##then flip that value

    '''
    Now looking at the values, it's time to sieve them out. We know 2 and 3 are prime, so start at 5 (4 is not prime) and go until the sqrt of the limit. If that value in the sieve is True, then I can loop through the array and remove any perfect squares of that value. Thus eliminating any of the future prime numbers
    '''
    for x in range(5,int((limit)**(1/2))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False

    ##Build array of prime numbers
    for p in range(5,limit):
        if sieve[p]:
            P.append(p)

    ##Return all of the primes below a given number
    return P

start = time.time()
all_primes = get_primes(999999)
six_digit_primes = [x for x in all_primes if len(str(x)) == 6]
print("Primes generated in {} seconds".format(round(time.time() - start, 4)))

def eightPrimes(s, rd):
    c=0
    for digit in '0123456789':
        n = int(s.replace(rd, digit))
        if isPrime(n) and n > 100000:
            c=c+1
    
    return c == 8

start = time.time()
for prime in six_digit_primes:
    s = str(prime)
    last_digit = s[5:6]
    if (s.count('0') == 3 and eightPrimes(s, '0')) \
     or (s.count('1') == 3 and eightPrimes(s, '1') and last_digit != '1') \
     or (s.count('2') == 3 and eightPrimes(s, '2')):
        print(s)
        
print("Found in {} seconds".format(round(time.time() - start, 4)))    


