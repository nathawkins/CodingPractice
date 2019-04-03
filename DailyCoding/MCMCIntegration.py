import random as r

def calcRadius(x,y):
    return (x**2+y**2)**(1/2)

R = 1
NUMITERS = 100000

hits = 0

for _ in range(NUMITERS):
    x = r.uniform(-R,R)
    y = r.uniform(-R,R)

    if calcRadius(x,y) <= R:
        hits += 1


print(4*R*hits/NUMITERS)