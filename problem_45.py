def Pent(num):
    if (1+(1+24*num)**(1/2)) % 6 ==0:
        return True
    else:
        return False

def Hex(num):
    if (1+(1+8*num)**(1/2)) % 4 ==0:
        return True
    return False

for val in range(286, 1000000000000000000000000000):
    triangle = val*(val+1)/2
    if Pent(triangle) and Hex(triangle):
        print(triangle)
        break
