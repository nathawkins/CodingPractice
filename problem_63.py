def powerLength(num, n):
    return len(str(num**n)) == n


counter = 0

for N in range(1,1000):
    for n in range(1,1000):
        if powerLength(N,n):
            print(N,n,N**n)
            counter += 1
        else:
            break

print(counter)