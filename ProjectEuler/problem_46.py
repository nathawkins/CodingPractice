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

start = time.time()

all_good = True
N = 9
while all_good:
    
    if isPrime(N):
        N += 2
        continue
    
    this_itr = False
    for ii in range(1,N):
        if this_itr:
            break
        for x in range(1,int(N**(1/2))+1):
            if isPrime(ii) and ii+2*x**2 == N:
                this_itr = True
                break
            
    if not this_itr:
        all_good = False
        print(N)
        
    else:
        N += 2
print(time.time()-start)
