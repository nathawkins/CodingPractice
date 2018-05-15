verify = []
for i in range(1,10):
    verify.append(str(i))

def is_pandigital(num):
    i = num
    num_l = list(str(num))
    factor = 2
    while True:
        i = num*factor
        num_l += list(str(i))
        factor += 1
        if len(num_l) >= 9:
            break


    s = sorted(num_l)
    if s == verify:
        return True, int(''.join(num_l))
    else:
        return False, 0

keeps = []

for x in range(9000, 10000):
    res = is_pandigital(x)
    if res[0]:
        print(x, res[1])
        keeps.append(res[1])
    else:
        continue

print(max(keeps))
