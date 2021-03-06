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

    ##Sum them up
    print("Sum of prime numbers up until {} is {}.".format(limit, sum(P)))

sieveOfAtkin(10)
sieveOfAtkin(100)
sieveOfAtkin(1000)
sieveOfAtkin(10000)
sieveOfAtkin(2000000)


# 142913828922
