def powerModulus(base, exp, c, m):
    return (c * pow(base, exp, m) + 1) % m

print("Last 10 digits = {}".format(powerModulus(2, 7830457, 28433, 10**10)))