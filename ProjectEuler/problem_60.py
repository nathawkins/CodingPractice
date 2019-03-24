'''
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the 
result will always be prime. For example, taking 7 and 109, both 7109 and 
1097 are prime. The sum of these four primes, 792, represents the lowest sum 
for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.
'''
import time

def get_primes(limit):
    '''Sieve of Atkin. Wrote this code for Problem 10'''
    P = [2,3]

    sieve=[False]*(limit+1)

    for x in range(1,int((limit)**(1/2))+1):

        for y in range(1,int((limit)**(1/2))+1):

            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5):
                sieve[n] = not sieve[n]

            n = 3*x**2+y**2
            if n<= limit and n%12==7: 
                sieve[n] = not sieve[n] 

            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11: 
                sieve[n] = not sieve[n]   

    for x in range(5,int((limit)**(1/2))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False

    for p in range(5,limit):
        if sieve[p]:
            P.append(p)
    return P

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

def getAllPermutes(val, list_of_primes):
    values = []
    for p in list_of_primes:
        res = allPermutations([val, p])
        for item in res:
            values.append(item)

    return values

def allPermutations(list_of_vals):
    permutes = []
    for i in range(len(list_of_vals)):
        for j in range(i+1, len(list_of_vals)):
            permutes.append(int(str(list_of_vals[i])+ str(list_of_vals[j])))
            permutes.append(int(str(list_of_vals[j])+ str(list_of_vals[i])))
    return permutes

def allPrime(list_of_vals):
    return not False in [isPrime(x) for x in list_of_vals]

primes = get_primes(10000)

def comb(a, b):
    len_a = len(str(a))
    len_b = len(str(b))
    if isPrime(int(a*(10**len_b)+b)) and isPrime(int(b*(10**len_a)+a)):
        return True
    return False

def solution():
    start = time.time()
    for a in primes:
        for b in primes:
            if b<a:
                continue
            if comb(a,b):
                for c in primes:
                    if c < b:
                        continue
                    if comb(a,c) and comb(b,c):
                        for d in primes:
                            if d<c:
                                continue
                            if comb(a,d) and comb(b,d) and comb(c,d):
                                for e in primes:
                                    if e<d:
                                        continue
                                    if comb(a,e) and comb(b,e) and comb(c,e) and comb(d,e) and comb(d,e):
                                        print(a,b,c,d,e)
                                        print(time.time() - start)
                                        return a+b+c+d+e

print(solution())