def Pn(n):
    return int(n*(3*n-1)*1/2)

def isPent(n):
    ##inverse function to see if number is pentagonal
    return (1+(24*n + 1)**(1/2))%6 == 0

min_diff = 0
min_1, min_2 = 0,0

i = 1

found = False

##while we haven't found our number
while not found:
    ##increment i to calculate the next pentagonal number
    i += 1

    ##calculate the pentagonal numbers
    num1 = Pn(i)

    ##starting at the pentagonal number before i
    j = i-1

    ##while that index is greater than zero
    while j > 0:
        ##calculate that pentagonal number
        num2 = Pn(j)

        ##if the sum and difference are both pentagonal
        if isPent(num1+num2) and isPent(abs(num1-num2)):
            ##store values, set found to be true, and break
            min_diff = abs(num1-num2)
            min_1, min_2 = num1, num2
            found = True
            break

        ##if not, decrement the value of j
        j -= 1

#print it all out at the end
print(i,j," : ",min_1, min_2, min_diff)
