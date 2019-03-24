def makeSpiral(spiral_size):
    mat = [[0 for x in range(spiral_size)] for x in range(spiral_size)]
    mid = int(spiral_size/2)
    mat[mid][mid] = 1

    i = mid
    j = mid+1

    current_val = 2

    while True:
        mat[i][j] = current_val
        current_val += 1


        ##stop condition to test
        if current_val == spiral_size**2+1:
            break

        if i+1 == len(mat) and j == 0:
            j += 1
            continue

        if i == len(mat):
            j += 1
            continue

        if i == len(mat) and j == len(mat[0]):
            break

         ##left side of the mat, go down the rows
        if j-1 < 0:
            i += 1
            continue

        ##right side of the mat, go up the rows
        if j+1 > len(mat[0]):
            i -= 1
            continue

        ##if we are in the top row, we only traverse the columns to the 
        ##0,0 index
        if i-1 < 0:
            j -= 1
            continue

        ##moving along the bottom row going to the right
        if i+1 > len(mat):
            j += 1
            continue

        ### now conditions for the spiral

        ##check diagonals for turning
        try:
            if mat[i+1][j+1] != 0 and mat[i][j-1] == 0 and mat[i-1][j] == 0 and mat[i+1][j] ==0:
                i += 1
                continue
        except:
            pass

        try:
            ##check diagonals for turning
            if mat[i-1][j+1] != 0 and mat[i][j-1] == 0 and mat[i+1][j] == 0 and mat[i][j+1] ==0:
                j += 1
                continue
        except:
            pass

        ##move downwards
        try:
            if mat[i+1][j] == 0 and mat[i][j+1] != 0 and mat[i-1][j] != 0:
                i +=1
                continue
        except:
            pass

        ##move right
        try:
            if mat[i][j-1] != 0 and mat[i-1][j] != 0 and mat[i][j+1] == 0:
                j +=1 
                continue
        except:
            pass

        ##element to the left is not zero and above
        ##is, then move up 
        if mat[i][j-1] != 0 and mat[i-1][j] == 0:
            i -= 1
            continue

        ##zero above and to the left, move to the left
        if mat[i][j-1] == 0 and mat[i-1][j] == 0:
            j -= 1
            continue

    return mat

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n%2==0 or n%3 == 0:
        return False
    
    r = int(n**0.5)
    f = 5
    ##anything that is divsible by an even number has
    ##to also be divisible by 2 or 3, so we don't
    ##need to check those, only 2,3,5 and then every odd
    ##power up to the sqrt of the maximum
    while f <= r:
        if n%f == 0 or n%(f+2) == 0:
            return False
        f += 6 ##hits all of the odd powers that aren't
               ##aren't divisible by 3
    return True

def printMat(mat):
    for i in mat:
        print(i)

def getDiags(spiral_size):
    if spiral_size == 1:
        return 1

    diags = [3,5,7,9]
    if spiral_size == 3:
        return diags

    for x in range(4, spiral_size, 2):
        for _ in range(4):
            diags.append(diags[-1]+x)

    return diags

def get_primes(limit):
    '''Sieve of Atkin. Wrote this code for Problem 10'''
    ##Start with the formation of an array that holds the prime numbers
    P = [2,3]

    ##Make an array of Boolean's, all False to begin with, of length limit
    sieve=[False]*(limit+1)

    ##Now do the sifting, checking x values up until the sqrt(limit)
    for x in range(1,int((limit)**(1/2))+1):

        ##y values cover the same limits
        for y in range(1,int((limit)**(1/2))+1):

            '''
            All numbers with modulo-sixty remainder 1, 13, 17, 29, 37, 41, 49, or 53 have a modulo-twelve remainder of 1 or 5.
            '''
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5): ##If the value of n is divisible by 12 and has remainder 1 and 5
                sieve[n] = not sieve[n]           ##then flip the value of that entry in the sieve array.


            '''
            All numbers with modulo-sixty remainder 7, 19, 31, or 43 have a modulo-six remainder of 1.
            '''
            n = 3*x**2+y**2
            if n<= limit and n%12==7:             ##If the value of n is divisible by 12 and has a remainder of 7
                sieve[n] = not sieve[n]           ##then flip that value


            '''
            n needs to be a positive solution, so we have to check and make sure x is greater than y. All numbers with modulo-sixty remainder 11, 23, 47, or 59 have a modulo-twelve remainder of 11.
            '''
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11:     ##If the value of n is divisible by 12 and has a remainder 11
                sieve[n] = not sieve[n]           ##then flip that value

    '''
    Now looking at the values, it's time to sieve them out. We know 2 and 3 are prime, so start at 5 (4 is not prime) and go until the sqrt of the limit. If that value in the sieve is True, then I can loop through the array and remove any perfect squares of that value. Thus eliminating any of the future prime numbers
    '''
    for x in range(5,int((limit)**(1/2))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False

    ##Build array of prime numbers
    for p in range(5,limit):
        if sieve[p]:
            P.append(p)

    ##Return all of the primes below a given number
    return P

def calcLenDiags(spiral_size):
    return 4*int(spiral_size/2)

def getPrimesTo(primes, val):
    these_primes = []
    for p in primes:
        if p <= val:
            these_primes.append(p)
        else:
            break

    return these_primes



i = 0
itr_amount = 1
ratio = 1
primes = []
all_numbers = [1]

while ratio > 0.1:
    ##adding one additional layer to the outside of the
    ##matrix adds four diagonal elements
    for _ in range(4):
        ##increment i to start
        i += itr_amount
        ##get an odd number out of this, 2n + 1 is always odd
        present_number = 2*i + 1
        ##add that to the list of elements which will lie along the diagonal
        ##all of them have to be odd, and every fourth is skipped,
        ##e.g. 1,3,5,7,9,13,17,21,25, and so on
        all_numbers.append(present_number)
        ##if it's prime, add it to the primes
        if isPrime(present_number):
            primes.append(2*i + 1)

        ##calculate the ratio of the numbers, then increase
        ##the amount we skip by 1 for each layer
    ratio = float(len(primes))/len(all_numbers)
    itr_amount += 1

print((2*i+1)**0.5)

# primes = get_primes(10000)
# primes = primes[1:]
# primes = [primes[i] for i in range(len(primes)) if (i+1)%4 != 0]

# i = 3
# while True:
#     tot_diags = calcLenDiags(i)
#     these_primes = getPrimesTo(primes, i**2)
#     if len(these_primes)/tot_diags < 0.10:
#         print(i, len(these_primes)/tot_diags)
#         break

#     i += 2


##other slow way using diagonal generation
# S = 7
# while True:
#     these_diags = getDiags(S)
#     primes = [x for x in these_diags if isPrime(x)]
#     if len(primes)/len(these_diags) <= 0.10:
#         print(S)
#         break
#     else:
#         print(S)
#     S += 2

##if using the super slow function to make a list 
##with spiral elements
# for S in range(3,1000,2):
#     this_mat = makeSpiral(S)
#     primes = []
#     counter = 0
#     for i in range(len(this_mat)):
#         counter += 2
#         if isPrime(this_mat[i][i]):
#             primes.append(this_mat[i][i])
        
#         if isPrime(this_mat[i][len(this_mat)-i-1]):
#             primes.append(this_mat[i][len(this_mat)-i-1])
#     counter -= 1
#     if len(primes)/counter <= 0.10:
#         print(S)
#         break
#     else:
#         print(S, len(primes)/counter)