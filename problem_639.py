from numba import jit
from time import time
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
    return list(set([int(x) for x in factorization]))

# @jit
# def fk(i,k = 1):
#     if i == 1:
#         return 1
#
#     else:
#         factors = primeFactors(i)
#         prod = 1
#         for val in factors:
#             prod *= val**k
#         return prod

@jit
def fk(i):
    if i == 1:
        return 1

    else:
        factors = primeFactors(i)
        prod = 1
        for val in factors:
            prod *= val
        return prod


# @jit
# def G(N, A):
#     total = 1*N
#     for i in range(2, A+1):
#         x = fk(i, 1)
#         total += x*(1-x**N)/(1-x)
#
#     return total
#

for i in range(1,101):
    print("i = {}. Factors = {}. fk_1({}) = {}.".format(i, primeFactors(i), i, fk(i)))

for i in range(1,101):
    # print("i = {}. Factors = {}. fk_1({}) = {}.".format(i, primeFactors(i), i, fk(i)))

    this_tot = 0
    for j in range(1,i+1):
        this_tot += fk(j)

    print("i = {}. Sk_1(i) = {}".format(i, this_tot))
