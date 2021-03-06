'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 
3330, is unusual in two ways: (i) each of the three terms are prime, 
and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

def sieveOfAtkin(limit):
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

    return P

primes = sieveOfAtkin(9999)
four_digit_primes = [p for p in primes if p >= 1000]


for p in four_digit_primes:
    ##get the prime number we are currently at
    this_p = p
    ##make a list of primes which satisfy our conditions,
    ##which to start is only one
    verified = [this_p]
    ##keep going until we are done
    while True:
        ##add 3330 to this prime
        next_p = this_p + 3330
        ##if it's a 4 digit prime and a permutation of our current prime
        if (next_p in four_digit_primes) and (str(this_p).strip(str(next_p)) == ""):
            ##keep it and increment what value we are at
            verified.append(next_p)
            this_p += 3330
        ##otherwise, we stop
        else:
            break
    
    ##if we get three values, print the joined number
    if len(verified) > 2:
        print("".join([str(x) for x in verified]))
