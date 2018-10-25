from numba import jit
from multiprocessing import Pool

@jit
def primeFactors(n):
    factorization = []

    ##Get all of the factors of two that may
    ##exist
    while n % 2 == 0:
        factorization.append(2)
        n = n / 2

    ##n must be odd at this point
    ##so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(n**0.5)+1,2):

        ##while i divides n
        while n % i== 0:
            factorization.append(i)
            n = n / i

    ##Condition if n is a prime
    ##number greater than 2
    if n > 2:
        factorization.append(n)

    ##return factorization
    return [int(x) for x in factorization]

@jit
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

@jit
def coprime(a, b):
    return gcd(a, b) == 1

@jit
def getTwoMults(factors):
    for ind in range(len(factors)):
        prod_1 = 1
        prod_2 = 1

        for i, val in enumerate(factors):
            if i <= ind:
                prod_1 *= val
            else:
                prod_2 *= val

        if coprime(prod_1, prod_2):
            break

    return prod_1, prod_2

base = {}

def fk(k,n):
    global base
    print(k,n)
    if n == 1:
        return 1

    try:
        return base[n]**k
    except:
        pass

    prime_factors_of_i = primeFactors(n)

    if len(set(prime_factors_of_i)) == 1:
        ##single unique prime factor, p
        base[n] = prime_factors_of_i[0]
        return base[n]**k

    prod1, prod2 = getTwoMults(prime_factors_of_i)

    base[n] = fk(k,prod1)*fk(k,prod2)
    return base[n]**k
#
# print(fk(1,2), fk(1,2) == 2)
# print(fk(1,4), fk(1,4) == 2)
# print(fk(1,18), fk(1,18) == 6)
# print(fk(2,18), fk(2,18) == 36)

@jit
def Sk(input_tuple):
    k,n = input_tuple
    print(k,n)
    total = 0
    for i in range(1,n+1):
        total += fk(k,i)
    return total

# print(Sk(1,10), Sk(1,10) == 41)
# print(Sk(1,100), Sk(1,100) == 3512)
# print(Sk(2,100), Sk(2,100) == 208090)

if __name__ == '__main__':
    K = 3
    A = int(1E6)
    pool = Pool(processes = 4)
    outputs = pool.map(Sk, [(k, A) for k in range(1,K+1)])
    pool.close()
    pool.join()
    total = sum(outputs)

    print(total%1000000007)
