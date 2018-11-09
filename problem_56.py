def digitSum(number):
    return sum([int(x) for x in str(number)])

max_sum = 0
sol = []

for a in range(1,101):
    for b in range(1,101):
        this_sol = [a,b,digitSum(a**b)]
        if this_sol[-1] > max_sum:
            max_sum = this_sol[-1]
            sol = this_sol[:-1]

print(sol)
print(max_sum)