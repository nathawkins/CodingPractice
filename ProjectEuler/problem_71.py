###Brute Force

d = 8

fracs = {}

for D in range(1,d+1):
    for N in range(1,D):
        frac_str = "{}/{}".format(N,D)
        fracs[frac_str] = N/D

fractions = sorted(list(fracs.keys()))
reduced_fractions = []
decimal_values = []
for frac in fractions:
    if fracs[frac] not in decimal_values:
        reduced_fractions.append(frac)
        decimal_values.append(fracs[frac])

sorting = [(val, i) for i,val in enumerate(decimal_values)]
sorting.sort()
sorted_fractions = [reduced_fractions[i[1]] for i in sorting]

where_37 = sorted_fractions.index("3/7")

print(sorted_fractions)
print(sorted_fractions[where_37-1])