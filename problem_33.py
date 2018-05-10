##Make strings to analyze for digits to cancel out
##Numerator and denominator have to both be two digits, so only need 10-99
numbers = [str(x+10) for x in range(90)]

def digit_in(str1, str2):
    str1_l = list(str1)
    str2_l = list(str2)
    for s in str1_l:
        if s in str2_l:
            return (True,s)
    return (False, "")

def get_inds(str1, str2):
    str1_l = list(str1)
    str2_l = list(str2)
    res, digit = digit_in(str1, str2)
    if res and '0' not in str2_l:
        return (str1_l.index(digit), str2_l.index(digit))
    else:
        return False

def stof(str1, str2):
    return int(str1)/int(str2)

numerators = []
denominators = []

for i in range(len(numbers)):
    test = numbers[i]
    for j in range(i+1, len(numbers)):
        base = numbers[j]
        if not get_inds(test, base):
            continue
        these_inds = get_inds(test, base)
        frac = stof(test[not these_inds[0]], base[not these_inds[1]])
        actual = stof(test, base)
        if frac == actual:
            print(test+'/'+base+' = '+test[not these_inds[0]]+'/'+base[not these_inds[1]]+' = '+str(actual))
            numerators.append(test[not these_inds[0]])
            denominators.append(base[not these_inds[1]])

print(numerators, denominators)
num = [int(x) for x in numerators]
den = [int(x) for x in denominators]

N = 1
D = 1
for i in range(len(num)):
    N *= num[i]
    D *= den[i]

print(N/D)
