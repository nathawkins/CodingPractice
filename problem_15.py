##Define the size of the cude that we want to work with
def route_num(cube_size):

    L = [1] * cube_size

    for i in range(cube_size):
        for j in range(i):
            ##Update the L[j]
            L[j] = L[j]+L[j-1]

        ##Update L[i]
        L[i] = 2 * L[i - 1]

    return L[cube_size - 1]

print(route_num(20))
