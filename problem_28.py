##N x N spiral grid
N = 1001

diags = 0

##The smallest spiral we can have is 3x3, and it increases by 2 every time
for n in range(3, N+1, 2):
    ##The values at the corners have a general form. No need to make a spiral
    top_right = n**2
    top_left = n**2 - n + 1
    bottom_right  = n**2 - 3*n +3
    bottom_left = n**2 - 2*n +2

    ##Add them all up
    diags += (top_right + top_left + bottom_right + bottom_left)

diags += 1

print(diags)
