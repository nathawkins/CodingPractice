'''
A common security method used for online banking is to ask
the user for three random characters from a passcode. For example,
if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters;
the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the
file so as to determine the shortest possible secret passcode of
unknown length.
'''

with open("problem_79_text.txt", 'r') as f:
    lines = f.readlines()

lines = [x.strip("\n") for x in lines]

passcode_digits = set(list("".join(lines)))
# print("Shortest passcode consists of", len(passcode_digits)," digits.")
# print(passcode_digits)

graph = {}

for dig in passcode_digits:
    graph[dig] = []

for code in lines:
    for i in range(len(code)-1):
        for j in code[i+1:]:
            if j not in graph[code[i]]:
                graph[code[i]] += [j]

vals = list(graph.values())
keys = list(graph.keys())
val_lengths = sorted([(keys[i], len(vals[i]),int(keys[i])) for i in range(len(vals))])

print(val_lengths)

key = ''
i = 0

while i < len(val_lengths):
    if val_lengths[i][1] == len(key):
        key = val_lengths[i][0] + key
        if len(key) == len(passcode_digits):
            i = 10000000
        else:
            i = 0
    i += 1

print(key)
