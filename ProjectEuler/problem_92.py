def squareDigitsNum(num_str):
    return str(sum(int(x)**2 for x in num_str))

memo = {}

def getChainEnd(num_str):
    while True:
        try:
            next_num = memo[num_str]
        except:
            next_num = squareDigitsNum(num_str)
            memo[num_str] = next_num

        if next_num == "89" or next_num == "1":
            break
        else:
            num_str = next_num

    return next_num


count_89 = 0
count_1 = 0

MAX = 1E7
MAX = int(MAX)+1

for N in range(1,MAX):
    res = getChainEnd(str(N))

    if res == "1":
        count_1 += 1
    else:
        count_89 += 1

print("End in 89: {}. End in 1: {}".format(count_89, count_1))

