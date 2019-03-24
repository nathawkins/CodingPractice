from numba import jit

@jit
def isPermutation(num1, num2):
    digits = [0,0,0,0,0,0,0,0,0,0]

    while num1:
        digits[num1 % 10] += 1
        num1 = int(num1 / 10)

    while num2:
        digits[num2 % 10] -= 1
        num2 = int(num2 / 10)

    total = 0
    for num in digits:
        if num != 0:
            return False

    return True

LIMIT = 10000

for num1 in range(345,LIMIT+1):
    count = 1
    nums = [num1]
    for num2 in range(num1+1,LIMIT+1):
        if isPermutation(int(num1**3), int(num2**3)):
            count += 1
            nums.append(num2)
        if len(str(num2**3)) > len(str(num1**3)):
            break
    if count >= 5:
        nums.sort()
        print(count,["{}^3:{}".format(x, x**3) for x in nums])
        break
