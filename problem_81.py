with open("problem_81_matrix.txt", "r") as f:
	mat = f.readlines()

matrix = []

for string in mat:
	row = string.strip("\n")
	row = [int(x) for x in row.split(",")]
	matrix.append(row)

##Testing matrix from website prompt
# matrix = [[131,673,234,103,18],
# 		  [201,96,342,965,150],
# 		  [630,803,746,422,111],
# 		  [537,699,497,121,956],
# 		  [805,732,524,37,331]]

R, C = len(matrix), len(matrix[0])

for i in range(R):
	for j in range(C):

		if i*j > 0:
			matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

		else:
			if i:
				matrix[i][j] += matrix[i-1][j]
			elif j:
				matrix[i][j] += matrix[i][j-1]
			else:
				matrix[i][j] += 0
				
print(matrix[-1][-1])