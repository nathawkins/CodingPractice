'''
proof:
a^2 + b^2 &= (p-a-b)^2\\
a^2 + b^2 &= p^2 + a^2 + b^2 - 2ap - 2bp + 2ab\\
0 &= p^2 - 2ap - 2bp+ 2ab\\
2ap + 2bp - 2ab &= p^2\\
b(2p - 2a) + 2ap &= p^2\\
b(2p-2a) &= p^2 - 2ap\\
b &= \frac{p^2 - 2ap}{2p-2a}\\
b &= \frac{p(p-2a)}{2(p-a)}


b &= \frac{p(p-2a)}{2(p-a)}\\
a &\leq b \\
a &\leq \frac{p(p-2a)}{2(p-a)}\\
2ap - 2a^2 &\leq p^2 - 2ap\\
4ap - 2a^2 -p^2 &\leq 0\\
2a^2 - 4ap + p^2 &\geq 0\\
a &\leq \frac{1}{2}  (2p-\sqrt{2} p)\\
a &\leq p - \sqrt{2}/2 p\\
a &\leq \frac{(2 - \sqrt{2}) p}{2}
'''

#p = 1000 ##maximum perimeter we are going for
#p = 120 ##for testing

def getTriangles(p):
    sols = []
    for a in range(1, int((2-2**(1/2))*p/2)+1):
        b = p*(p-2*a)/(2*(p-a))
        if int(b) == b:
            sols.append((a, b, (a**2+b**2)**(1/2) ))
    return sols

num, p_max = 0,0
for p in range(1,1000):
    result = getTriangles(p)
    if len(result) > num:
        num,p_max = len(result),p

print(num, p_max)
