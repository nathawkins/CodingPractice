factorials = {1:1, 2:2, 3:6}
sum_of_digits = {1:1, 2:2, 3:6}

largest_number = 100

for num in range(4, largest_number+1):
    ##Number we want to find the factorial of
    max_num = num
    ##Doing the n x n-1 x n-2 .. 3 x 2 x 1
    times_by = max_num-1
    ##keping track of the value of the factorial
    factorial = max_num
    while times_by > 0:
        if factorials.get(times_by, False) != False:
            factorial *= factorials.get(times_by, False)
            break
        factorial *= times_by
        times_by -= 1
    factorials[max_num] = factorial

    ##Sum the digits in the factorial
    digit_list = list(str(factorial))
    fact_sum = 0
    for digit in digit_list:
        fact_sum += int(digit)
    sum_of_digits[max_num] = fact_sum

print(sum_of_digits.get(largest_number, False))
