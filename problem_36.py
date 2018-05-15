def bin_string(i):
    s = str(bin(i))
    return s[2:]

def is_palindrome(s):
    return s == s[::-1]

double_base_palindromes = []

for x in range(1000000):
    if is_palindrome(str(x)):
        s = bin_string(x)
        if is_palindrome(s):
            double_base_palindromes.append(x)
        else:
            continue
    else:
        continue

print(sum(double_base_palindromes))
