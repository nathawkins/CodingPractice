limit = 100

terms = []

for a in range(2, limit+1):
    for b in range(2, limit+1):
        terms.append(a**b)

print(len(list(set(terms))))
