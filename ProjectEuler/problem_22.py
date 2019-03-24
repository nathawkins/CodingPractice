##Setup dictionary to score the names
alphabet = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

##Read in the names from the text file
with open("problem_22-text.txt","r") as filename:
    names = filename.readlines()

##The data is a little funky, so clean it up by removing unnecessary punctuation
names = names[0].split(",")
names = [name.replace('"', '') for name in names]

##Sort the names based on the strings
names.sort(key = str.lower)

##Keep track of the total score
total_score = 0

##Perform the scoring of each of the names
for i in range(len(names)):
    score = i+1
    letter_sum = 0
    letters = list(names[i].lower())
    for letter in letters:
        letter_sum += alphabet.get(letter, False)

    total_score += (score * letter_sum)

##The total score is!
print(total_score)
