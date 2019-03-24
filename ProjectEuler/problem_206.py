def isMatch(num):
    num_s = str(num)
    return not all(int(num_s[x*2]) == x+1 for x in range(9))


n = 138902663

while isMatch(n*n):
    n -= 2

print(n*10, (n*10)**2)
