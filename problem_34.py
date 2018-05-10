def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

facts = [factorial(x) for x in range(10)]

results = []

for x in range(3,factorial(9)*8):
# for x in range(3, 200):
    number = list(str(x))
    fac_sum = sum([facts[int(y)] for y in number])
    if fac_sum == x:
        results.append(x)

print(sum(results))
