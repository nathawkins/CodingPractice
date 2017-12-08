how_many_doors = 100

doors = []
for i in range(1,how_many_doors+1):
    doors.append(i)

doors_light = [1 for i in range(len(doors))]

if how_many_doors > 1000:
    print("Doors still with lights on:",[k for k in range(1,how_many_doors+1) if k%k**(1/2) == 0])

else:
    for j in range(2,len(doors)+1):
        for k in doors:
            if k%j == 0:
                if doors_light[k-1] == 1:
                    doors_light[k-1] = 0
                else:
                    doors_light[k-1] = 1
    print("Doors still with lights on:",[k for k in range(1,len(doors)+1) if doors_light[k-1] == 1])
