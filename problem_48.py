compound = 0

for i in range(1,1001):
    this_num = i**i
    compound += this_num

print(str(compound)[-10:])