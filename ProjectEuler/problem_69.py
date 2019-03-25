def isPrime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f += 6
    return True  

def getPrimorialPrimes(MAX):
    primesNeeded = []
    total_prod = 1
    num = 2
    while True:
        if isPrime(num):
            primesNeeded.append(num)
            total_prod *= num
        num += 1
        if total_prod > MAX:
            break
    return primesNeeded

def findSolution(MAX):
    primes = getPrimorialPrimes(MAX)
    maxn = 1
    for p in primes:
        if maxn*p > MAX: return maxn
        maxn *= p
    return -1

print(findSolution(1000000))