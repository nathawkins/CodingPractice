import sympy as sym

x = sym.symbols('x')

class DicePlayer:
    def __init__(self, N_dice, N_sides):
        self.N_sides = N_sides
        self.sides = [x for x in range(1,N_sides+1)]
        self.N = N_dice

    def getRollCombos(self):
        self.polynomial = sym.Poly([1]*(self.N_sides+1), x)
        self.polynomial -= 1
        self.roll_combos = self.polynomial**self.N
        self.combinations = self.roll_combos.coeffs()
        self.roll_table = {}
        for i,ind in enumerate(range(self.N*min(self.sides), (self.N*max(self.sides))+1)):
            self.roll_table[ind] = self.combinations[i]


Pete = DicePlayer(9, 4)
Pete.getRollCombos()
Colin = DicePlayer(6,6)
Colin.getRollCombos()

p = Pete.roll_table
c = Colin.roll_table

for key in list(c.keys()):
    try:
        p[key] += 0
    except:
        p[key] = 0

for key in list(p.keys()):
    try:
        c[key] += 0
    except:
        c[key] = 0

denominator = Pete.N_sides**Pete.N * Colin.N_sides**Colin.N
numerator = 0

for C in list(c.keys()):
    for P in list(p.keys()):
        if P > C:
            numerator += c[C]*p[P]

print(round(numerator/denominator,7))