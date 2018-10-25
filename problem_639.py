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

def areFactorsPower(factors):
    ##If there is only 1 unique factor, then the number
    ##must be able to be represented as a power of a factor
    return len(set(factors)) == 1 and len(factors) != 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

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


# computed_fk = {}

def fk(k,i):
    # global computed_fk

    # try:
    #     return computed_fk[(k,i)]
    # except:
    #     pass

    if i == 1:
        return 1

    factors_of_i = primeFactors(i)

    print(factors_of_i)

    if areFactorsPower(factors_of_i):
        e = len(set(factors_of_i))
        p = list(set(factors_of_i))[0]
        # computed_fk[(k,i)] = p**k
        return p**k

    if len(factors_of_i) == 1:
        p = factors_of_i[0]
        # computed_fk[(k,i)] = p**k
        return p**k

    else:
        int1, int2 = getTwoMults(factors_of_i)
        res = fk(k,int1)*fk(k,int2)
        # computed_fk[(k,i)] = res
        return res

# print(fk(1,2), fk(1,2) == 2)
# print(fk(1,4), fk(1,4) == 2)
print(fk(1,18), fk(1,18) == 6)
# print(fk(2,18), fk(2,18) == 36)

# print(computed_fk)

# def Sk(k,n):
#     total = 0
#     for i in range(1,n+1):
#         # print("k = {}, i = {}".format(k,i))
#         total += fk(k,i)
#
#     return total

# print(Sk(1,10), Sk(1,10) == 41)
# print(Sk(1,100), Sk(1,100) == 3512)
# print(Sk(2,100), Sk(2,100) == 208090)


# def G(N,A):
#     total = 0
#     for k in range(1,N+1):
#         # print("k = {}".format(k))
#         total += Sk(k, A)
#     return total

# print(G(3, 10))
# print(G(3, int(1E8))%1000000007 == 338787512)
# print(G(50, int(1E12))%1000000007)
