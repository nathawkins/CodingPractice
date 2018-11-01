from numba import jit
from time import time
from multiprocessing import Pool, cpu_count

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

@jit
def fk(i,k):
    if i == 1:
        return 1

    else:
        factors = primeFactors(i)
        prod = 1
        for val in factors:
            prod *= val**k
        return prod

@jit
def fkt(t):
    i, k = t[0], t[1]
    if i == 1:
        return 1

    else:
        factors = primeFactors(i)
        prod = 1
        for val in factors:
            prod *= val**k
        return prod

@jit
def Sk(N, k):
    total = 0
    for i in range(1, N+1):
        total += fk(i, k)
    return total

# start = time()
# print(Sk(int(1E7),1))
# print(time() - start)
# ###221 seconds to run above code -- 35222287961010


if __name__ == '__main__':
    # def SkP(N,k):
    #     pool = Pool(processes = int(cpu_count()/2))
    #     total = sum(pool.map(fkt, [(x, k) for x in range(1, N+1)]))
    #     pool.close()
    #     pool.join()
    #     return total

    # start = time()
    # print(SkP(int(1E7),1))
    # print(time() - start)
    # ###cpu_count/2, 141 seconds -- 35222287961010

    def SkP(N,k):
        pool = Pool(processes = cpu_count())
        total = sum(pool.map(fkt, [(x, k) for x in range(1, N+1)]))
        pool.close()
        pool.join()
        return total

    start = time()
    print(SkP(int(1E7),1)) ###1E8 floors memory
    print(time() - start)
    ###cpu_count, 103 seconds -- 35222287961010 (laptop)
    ###cpu_count, 73 seconds -- 35222287961010 (machine)
