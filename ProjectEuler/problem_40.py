import time
start = time.time()
res = "123456789"

std = [0,1,2,3,4,5,6,7,8,9]
std = [str(x) for x in std]

BOUND = 1000000

k = 1
while len(res) < BOUND:
    for val in std:
        res += str(k)+val
    k += 1

inds = [1,10,100,1000,10000,100000,1000000]

prod = 1
for ind in inds:
    try:
        prod *= int(res[ind-1])
    except:
        pass
print(round(time.time() -start, 2))
print(prod)
