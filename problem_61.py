def triangle(n):
    return n*(n+1)/2

def square(n):
    return n**2

def pentagonal(n):
    return n*(3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

def heptagonal(n):
    return n*(5*n-3)/2

def octogonal(n):
    return n*(3*n-2)

def getNumberList(function, min = 1000,  max = 10000):
    results = []
    n = 1
    while True:
        this_num = function(n)
        if this_num >= max:
            break
        if this_num > min:
            results.append(this_num)
        n += 1
    return results

triangles = getNumberList(triangle)
squares = getNumberList(square)
pentagonals = getNumberList(pentagonal)
hexagonals = getNumberList(hexagonal)
heptagonals = getNumberList(heptagonal)
octogonals = getNumberList(octogonal)

triangles = [t for t in triangles if t not in hexagonals]

lists = [triangles, squares, pentagonals, hexagonals, heptagonals, octogonals]

all_nums = triangles+squares+pentagonals+hexagonals+heptagonals+octogonals
all_nums = [int(x) for x in list(set(all_nums))]
all_nums = [x for x in all_nums if str(x)[-2] != "0"]

def do_it():
    for a in all_nums:
        for b in all_nums:
            if a == b:
                continue
            if str(a)[-2:] == str(b)[:2]:
                for c in all_nums:
                    if a == c or b == c:
                        continue
                    if str(b)[-2:] == str(c)[:2]:
                        for d in all_nums:
                            if a == d or b == d or c == d:
                                continue
                            if str(c)[-2:] == str(d)[:2]:
                                for e in all_nums:
                                    if a == e or b == e or c == e or d == e:
                                        continue
                                    if str(d)[-2:] == str(e)[:2]:
                                        for f in all_nums:
                                            if a == f or b == f or c == f or d == f or e == f:
                                                continue
                                            if str(e)[-2:] == str(f)[:2] and str(f)[-2:] == str(a)[:2]:
                                                possible_sol = [a,b,c,d,e,f]
                                                res = [0]*len(lists)
                                                for item in possible_sol:
                                                    this_bool = [item in l for l in lists]
                                                    for i in range(len(this_bool)):
                                                        if this_bool[i]:
                                                            res[i] += 1
                                                if 0 not in res:
                                                    print(sum(possible_sol))
                                                    return possible_sol

do_it()
