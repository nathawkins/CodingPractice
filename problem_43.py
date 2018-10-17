def isPandigital(n):
    return not "0123456789".strip(str(n))


def strDivisibility(n):
    sub_numbers = []
    for i in range(len(n)-3):
        this_sub_nums = n[i+1:i+4]
        sub_numbers.append(int("".join(this_sub_nums)))
    checks = [2,3,5,7,11,13,17]
    
    ary = [sub_numbers[i]%checks[i] == 0 for i in range(len(checks))]

    return all(ary)

'''
Proof:
\mathcal{S} &= \{1,2,3,4,5,6,7,8,9,0\}\\
d_4 d_5 d_6 \% 5 &= 0\\
d_6 &= (0,5)\\
d_6 d_7 d_8 \% 11 &= 0\\
d_6 &= 5\ \text{ and } d_7 \text{ or } d_8 \neq 5\\
\mathcal{S} &= \{1,2,3,4,6,7,8,9,0\}\\
d_6 d_7 d_8 &= (506, 517, 528, 539, 561, 572, 583, 594)\\
d_7 d_8 d_9 \% 13 &= 0\\
d_7 d_8 d_9 &= (286, 390, 728, 832)\\
d_8 d_9 d_{10} \% 17 = 0\\
d_8 d_9 &= (86, 90, 28, 32) \\
d_8 d_9 d_{10} &= (289, 867, 901)\\
d_6 &= 5\\
d_7 &= (7,2,3)\\
d_6 d_7 d_8 d_9 d_{10} &= (57289, 52867, 53901)\\
d_5 d_6 d_7 \% 7 = 0\\
d_5 d_6 d_7 &= (357, 952)\\
d_5 d_6 d_7 d_8 d_9 d_{10} &= (357289, 952867)\\
d_3 d_4 d_5 &= (063, 603, 309)\\
d_3 d_4 d_5 d_6 d_7 d_8 d_9 d_{10} &= (06357289, 60357289, 30952867)\\
d_1 d_2 &= (14, 41)\\
\therefore \mathcal{N} &= (1406357289, 4106357289, 1460357289, 4160357289, 1430952867, 4130952867)\\
'''


to_check = [1406357289, 1430952867, 1460357289, 4106357289, 4130952867, 4160357289]

total = 0

for val in to_check:
    if isPandigital(str(val)) and strDivisibility(str(val)):
        total += val

print(total)
