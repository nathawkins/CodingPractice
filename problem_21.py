def get_divisors(num):
    this_a = num
    a_factors = []
    ##Largest factor is half of the value
    for i in range(int(num/2), 0, -1):
        if this_a%i == 0:
            a_factors.append(i)
    return(sum(a_factors))


amicable_nums = []
for i in range(1, 10000):
    ##The value to calculate it
    num = i

    ##Do the amicable calculations
    d = get_divisors(num)
    n = get_divisors(d)

    ##If n == num, if the two calculations equate
    if n == num and d != num:
        amicable_nums.append(d)
        amicable_nums.append(num)

##I don't care about doubles, I'll get rid of them by making is a set and then
##a list again
amicable_nums = set(amicable_nums)
amicable_nums = list(amicable_nums)

print(amicable_nums)
print(sum(amicable_nums))
