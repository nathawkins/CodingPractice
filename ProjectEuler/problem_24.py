##Digits I am finding the permutation of
digits = [0,1,2,3,4,5,6,7,8,9]

##Calculate the factorial of a number
def factorial(num):
    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    return factorial

##Digits to use to make permutation, each can only be used once
digits_to_use = [0,1,2,3,4,5,6,7,8,9]

##Which lexicographical factor I want
which_lp = 1000000

##Remove the factor of 0! = 1
which_lp -= 1

##Keep track of the permutation
lp = ''

##Looping through the digits that I have to work with
for k in range(1,len(digits)):
    ##Starting at 9! and working down to 1!
    digit = digits[-k]

    ##Calculate the value of this factorial
    this_fact = factorial(digit)

    ##Combinatorics method. We want to find out how many permutations this digit
    ##accounts for. Find the integer division of whatever value of which_lp
    ##we have divided by this factorial
    this_division = int(which_lp/this_fact)

    ##Use that result to index the digits_to_use. For instance, 1000000/9! = 2.
    ##So reference the second value in the digits to use array. Store that digit.
    lp += str(digits_to_use[this_division])

    ##Now, reduce which_lp by a factor of the division times the value of the factorial
    which_lp -= this_division*this_fact

    ##Remove the digit found in this iteration so we get a permutation that uses each digit once
    digits_to_use.remove(digits_to_use[this_division])

##Whatever factor is missing, tack it on at the end as it is the only remaining digit
lp_list = list(lp)
for val in digits:
    if str(val) not in lp_list:
        lp_list.append(str(val))
        break

print(lp_list)
