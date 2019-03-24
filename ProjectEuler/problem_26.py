##Up to what denominator?
d = 1000

##Dictionary to keep track of the repeats, store in memory more efficiently
repeats = {}

##Starting with 1/2 and going up to 1/d
for i in range(2,d+1):
    ##Keep track of the remainders of the divisions
    remainders = []
    val = 1
    con = True
    while con:
        ##Start with 1%i and take the remainder, if it's not in the remainders array,
        ##then take that remainder and set the next division to be 10*val%i
        x = val%i
        if x in remainders or x == 0:
            ##Once we hit a repeat or the division is clean, then store the value
            repeats[i] = len(remainders)
            con = False
        else:
            remainders.append(x)
            val = 10*x

##Get the index with the maximum recurring cycle
print(max(repeats, key = repeats.get))
