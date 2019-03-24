CONSECUTIVE_CONST = 4
FACTORS_CONST = 4
MAXIMUM = 1000000
##It could go beyond our maximum value by some amount
MAXIMUM += CONSECUTIVE_CONST - 1


##Make a list for all numbers to see how many prime factors each has
prime_factors = [0]*MAXIMUM

##Starting at the number 2, index 2, up until the max
for i in range(2, MAXIMUM):
    ##If that value is 0, it is a prime and we need to increment
    ##all multiples of that value by one
    if prime_factors[i] == 0:
        ##For every multiple of that number
        for j in range(i, MAXIMUM, i):
            ##Add 1, it's a unique prime factor for a number
            prime_factors[j] += 1

##Initialize value for how many in a row this is
current_streak = 0

##Starting with the number 2
for k in range(2, MAXIMUM):
    ##If that value has a number of prime factors that we are
    ##looking for
    if prime_factors[k] == CONSECUTIVE_CONST:
        ##Increment the streak by 1
        current_streak += 1

        ##If we have hit our mark, show the streak with the
        ##correct prime factorizations
        if current_streak >= CONSECUTIVE_CONST:
            print([x for x in range(k - CONSECUTIVE_CONST+1,k+1)])
            break

    ##Otherwise, we reset the count
    else:
        current_streak = 0


'''
Brute Force
approx 74 seconds
'''
# import time
# CONSECUTIVE_CONST = 4
# FACTORS_CONST = 4
#
# MAXIMUM = 20
# def isPrime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n%2 == 0 or n%3 == 0:
#         return False
#
#     r = int(n**0.5)
#
#     f = 5
#
#     while f <= r:
#         if n%f == 0 or n%(f+2) == 0:
#             return False
#         f += 6
#     return True
#
# def primeFactors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors
#
# def product(list_of_factors):
#     prod = 1
#     for val in list_of_factors:
#         prod *= val
#     return prod
#
# factorization = {}
#
# start = time.time()
#
# for N in range(MAXIMUM):
#
#     prime_factors = primeFactors(N)
#
#     if len(prime_factors) == 0:
#         continue
#
#     if product(prime_factors) != N:
#         continue
#
#     if len(set(prime_factors)) != FACTORS_CONST:
#         continue
#
#     factorization[N] = prime_factors
#
# def getSequence(list_of_vals, starting_ind, length):
#     if starting_ind + length < len(list_of_vals):
#         return list_of_vals[starting_ind:starting_ind+length]
#     return list_of_vals[starting_ind:]
#
# def isConsecutive(sequence):
#     for i in range(len(sequence)-1):
#         if sequence[i+1] != sequence[i]+1:
#             return False
#     return True
#
#
# keys = list(factorization.keys())
# keys.sort()
#
# for i in range(len(keys)):
#     this_seq = getSequence(keys, i, CONSECUTIVE_CONST)
#     if isConsecutive(this_seq):
#         all_correct_length = True
#         for key in this_seq:
#             these_prime_factors = factorization[key]
#             if len(set(these_prime_factors)) != FACTORS_CONST:
#                 all_correct_length = False
#                 break
#         if not all_correct_length:
#             continue
#         else:
#             consecs = this_seq
#             break
#
# print(time.time() - start)
#
# try:
#     print(consecs)
# except:
#     print("Sequence Not Found")
