def nextFrac(frac_str):
    symbol_ind = frac_str.index("/")
    num = frac_str[:symbol_ind]
    den = frac_str[symbol_ind+1:]
    
    adding_num = str(int(den))
    
    new_num = str(int(num) + int(adding_num))

    num = den
    den = new_num

    num = str(int(num) + int(den))

    return num+"/"+den


def numLengthGreater(frac_str):
    symbol_ind = frac_str.index("/")
    num = frac_str[:symbol_ind]
    den = frac_str[symbol_ind+1:]
    return len(num) > len(den)

current_sol = "3/2"

count = 0

for x in range(1000):
    current_sol = nextFrac(current_sol)
    if numLengthGreater(current_sol):
        count += 1

print(count)