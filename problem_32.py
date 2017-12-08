##Pandigital list
l = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

##Verification set, easy to match and removes duplicates
verification = set(l)

##Keep track of the special products
products = []

'''In order to get 9 digits total between the multiplier, the multiplicand, and
the product, we can either multiply a 1 digit number by a 4 digit number, which gives a maximum of 5 digit number (total 10, minimum 9) or a 2 digit number by a 3 digit number to get a maximum of 5 digit product (10 total, 9 minimum). So, the loops for the multiplicand, goes from 1-99 (2 digit number) and the multiplier from 101 - 10000/multiplicand (we want a 4 digit maximum multiplier, so cap out at the smallest 5 digit number/multiplier, including the endpoints).'''
for i in range(1, 100):
    for j in range(101, int(10000/i)+1):
        prod = i*j
        this_m = []
        ##Turn it into a list with all of the characters
        this_m += list(str(i))
        this_m += list(str(j))
        this_m += list(str(prod))
        ##If we have 9 digits total across the three terms
        if len(this_m) == len(l):
            ##if each digit appears only once, retain it's value
            if set(this_m) == verification:
                products.append(prod)

##Get rid of any duplicate products
products = list(set(products))

##Print the sum, all pandigital fancy sums
print(sum(products))
