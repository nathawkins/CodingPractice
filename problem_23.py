##Calculate the sum of the divisors for an input number
def get_divisors(num):
    divs = [1]
    ##Check values from 2 to sqrt(num). 1 is included because everything
    ##is divisible by 1.
    for i in range(2,int((num**(1/2)))+1):
        ##If the number divides cleanly, keep both i and num/i.
        ##This is because num/i = k and num/k = i are both divisors to keep
        if num%i == 0:
            divs.extend([i,num/i])
    ##Filter out only the unique values and sum over them
    return sum(list(set(divs)))

##Is the number abundant?
def is_abundant(num):
    return get_divisors(num) > num

##All of the abundant numbers between 12 (smallest) and max range (28123)
abundant = [x for x in range(12, 28123) if is_abundant(x)]

##Assume that every number can be written as the sum of two abundant numbers
non_ab_sum = [x for x in range(28123)]

##For each abundant number
for i in range(len(abundant)):
    ##For every other abundant number we need to
    ##check between that abundant number and the max range
    for j in range(i, 28123):
        ##If the sum of these abundant numbers is less than the peak range
        ##then we know two abundant numbers sum to give us something in our range
        if abundant[i] + abundant[j] < 28123:
            ##Value goes to 0 to not be included in the final sum
            non_ab_sum[abundant[i]+abundant[j]] = 0
        ##If we can't write out this number as a sum of two abundant numbers,
        ##move on
        else:
            break

##Return the sum
print(sum(non_ab_sum))
