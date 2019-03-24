##Two ways to do this kind of problem

##Keep track of the possible combinations
counter = 0

'''
200 = x1*200 + x2*100 + x3*50 + x4*20 + x5*10 + x6*5 + x7*2 + x8*1
The obvious combination is to use a 2 pound coin. Remove that from the equation and add
1 to the final count. With that being known, the maximum number of 100 pence coins
that I can use is two, so looping through x2 from 0 -> 2. Next, the number of
50 pence coins I can use is (200 - x2*100)/50 = x3. This sets up the next loop, but
add one to account for including the eng point (using 4 50 pence coins). Next, the
possible combinations of 20 pence coins is (200-x2*100 - x3*50)/20 = x4. This continues
down the line until every combination has been solved for. Not including the one pence
coins because after figuring out how many 2 pence coins are needed, the one pence coins are just
added to give the total of 200, but the actual number of them needed doesn't matter. I care
about the unique combinations.
'''

target = 200

# number of 100p coins
for x2 in range(int(target/100)+1):
	# number of 50p coins
		for x3 in range(int(1+(target-100*x2)/50)):
			# number of 20p coins
				for x4 in range(int(1+(target-100*x2-50*x3)/20)):
					# number of 10p coins
						for x5 in range(int(1+(target-100*x2-50*x3-20*x4)/10)):
							# number of 5p coins
								for x6 in range(int(1+(target-100*x2-50*x3-20*x4-10*x5)/5)):
									# number of 2p coins
										for x7 in range(int(1+(target-100*x2-50*x3-20*x4-10*x5-5*x6)/2)):
											counter += 1

# Total number of ways we can form the 200p
# Added 1 for 200p case
print(counter+1)


##What coins do I have?
coins = [1, 2, 5, 10, 20, 50, 100, 200]

##Target sum of money
target = 200

##Building up all of the combinations below 200p
combinations = []
for j in range(target+1):
    combinations.append(0)
combinations[0] = 1

##For each coin
for i in range(len(coins)):
    ##Starting from the denomination of the coin up to the target amount
    for j in range(coins[i], target+1):
        ##The number of ways to get the sum total at index j is
        ##the ways in which the denominations below this sum divide into
        ##the sum total.
        '''
        i = 1 (2p coins)
        find all of the divisions from 2 to 200 that can be made with only 2p
        coins, keep track of those
        i = 2 (5p coins)
        add all of the divisions from 5 to 200 that cna be made using only 5p
        coins, add to sum total
        etc.
        '''
        combinations[j] += combinations[j-coins[i]]

##how many ways can we make 200? Last element of array
print(combinations[-1])
