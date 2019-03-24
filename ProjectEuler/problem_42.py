alphabet = {}
alpha_string ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for ind, letter in enumerate(alpha_string):
    alphabet[letter] = ind+1

with open("problem_42_words.txt","r") as f:
    words = f.readlines()

words = words[0].split(",")

def tn(n):
    return int(1/2*n*(n+1))

LIMIT = 2000

nums_to_check = [tn(N) for N in range(1,LIMIT)]

triangle_count = 0

for word in words:
    this_char_num = 0
    for char in word:
        if char in alpha_string:
            this_char_num += alphabet[char]
    if this_char_num in nums_to_check:
        triangle_count += 1

print(triangle_count)
