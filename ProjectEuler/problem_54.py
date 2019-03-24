card_vals = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7,
            '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 
            'A':14}


def all(val_list):
    return not False in val_list

def sameSuit(hand_list):
    res = ""
    for item in hand_list:
        res += item[-1]

    return res.strip(res[0]) == ""

def isConsecutive(hand_list):
    card_string = "".join([str(x[0]) for x in hand_list])
    cards = [card_vals[c] for c in card_string]
    cards = sorted(cards)
    order_bool = [cards[i+1] == cards[i]+1 for i in range(0, len(card_string)-1)]
    return all(order_bool)

def counter(hand_list):
    counter_dict = {}
    card_str = "".join(hand_list)
    for c in hand_list:
        counter_dict[c[0]] = card_str.count(c[0])

    return counter_dict

def royalFlush(hand_list):
    return sameSuit(hand_list) and isConsecutive(hand_list)

def onePair(hand_list):
    these_values = [card_vals[x[0]] for x in hand_list]
    these_values.sort()
    hand_count = counter(hand_list)
    if 2 not in list(hand_count.values()):
        return False, None

    else:
        scoring = 0
        cofactor = 0.1
        for k in list(hand_count.keys()):
            if hand_count[k] == 2:
                scoring += card_vals[k]
                break
            
        for val in these_values[::-1]:
            if val != scoring:
                scoring += val * cofactor
                cofactor /= 100
        
        return True, scoring

def twoPair(hand_list):
    these_values = [card_vals[x[0]] for x in hand_list]
    these_values.sort()
    hand_count = counter(hand_list)
    count_str = "".join(sorted( [str(x) for x in list(hand_count.values())] ))
    if "22" not in count_str:
        return False, None

    else:
        scoring = 0

        pairs = []
        remaining = []

        for k in list(hand_count.keys()):
            if hand_count[k] == 2:
                pairs.append(card_vals[k])
            else:
                remaining.append(card_vals[k])
            
        scoring += max(pairs)
        scoring += 0.01*min(pairs)
        scoring += 0.0001*remaining[0]

        return True, scoring

def threeOfAKind(hand_list):
    these_values = [card_vals[x[0]] for x in hand_list]
    these_values.sort()
    hand_count = counter(hand_list)
    if 3 not in list(hand_count.values()):
        return False, None

    else:
        scoring = 0
        cofactor = 0.1
        for k in list(hand_count.keys()):
            if hand_count[k] == 3:
                scoring += card_vals[k]
                break
            
        for val in these_values[::-1]:
            if val != scoring:
                scoring += val * cofactor
                cofactor /= 100
        
        return True, scoring

def fourOfAKind(hand_list):
    these_values = [card_vals[x[0]] for x in hand_list]
    these_values.sort()
    hand_count = counter(hand_list)
    if 4 not in list(hand_count.values()):
        return False, None

    else:
        scoring = 0
        cofactor = 0.1
        for k in list(hand_count.keys()):
            if hand_count[k] == 4:
                scoring += card_vals[k]
                break
            
        for val in these_values[::-1]:
            if val != scoring:
                scoring += val * cofactor
                cofactor /= 100
        
        return True, scoring

def straightFlush(hand_list):
    these_values = [card_vals[x[0]] for x in hand_list]
    these_values.sort()

    scoring = 0
    cofactor = 1
    for val in these_values[::-1]:
        scoring += cofactor*val
        cofactor /= 100

    return scoring

def fullHouse(hand_list):
    these_values = [card_vals[x[0]] for x in hand_list]
    these_values.sort()
    hand_count = counter(hand_list)
    if [2,3] != sorted(list(hand_count.values())):
        return False, None

    else:
        scoring = 0
        cofactor = 0.1
        for k in list(hand_count.keys()):
            if hand_count[k] == 3:
                scoring += card_vals[k]
                break

        for val in these_values[::-1]:
            if val != scoring:
                scoring += val * cofactor
                cofactor /= 100

        return True, scoring



def scoreHand(hand_list):
    if royalFlush(hand_list):
        return 10000

    if sameSuit(hand_list) and isConsecutive(hand_list):
        return 9000 + straightFlush(hand_list)

    if fourOfAKind(hand_list)[0]:
        return 8000 + fourOfAKind(hand_list)[1]

    if fullHouse(hand_list)[0]:
        return 7000 + fullHouse(hand_list)[1]

    if sameSuit(hand_list):
        return 6000 + straightFlush(hand_list)

    if isConsecutive(hand_list):
        return 5000 + straightFlush(hand_list)

    if threeOfAKind(hand_list)[0]:
        return 4000 + threeOfAKind(hand_list)[1]

    if twoPair(hand_list)[0]:
        return 3000 + twoPair(hand_list)[1]

    if onePair(hand_list)[0]:
        return 2000 + onePair(hand_list)[1]
    
    return max([card_vals[x[0]] for x in hand_list])

scores = {"P1":0, "P2":0}

def scoreRound(player_1_hand, player_2_hand):
    p1_score = scoreHand(player_1_hand)
    p2_score = scoreHand(player_2_hand)

    if p1_score > p2_score:
        # print("Player 1")
        scores["P1"] += 1
        return 0

    if p1_score < p2_score:
        # print("Player 2")
        scores["P2"] += 1
        return 0

# scoreRound(["5H", "5C", "6S", "7S", "KD"], ["2C", "3S", "8S", "8D", "TD"])
# scoreRound(['5D', '8C', '9S', 'JS', 'AC'], ['2C', '5C', '7D', '8S', 'QH'])
# scoreRound(['2D', '9C', 'AS', 'AH', 'AC'], ['3D', '6D', '7D', 'TD', 'QD'])
# scoreRound(['4D', '6S', '9H', 'QH', 'QC'], ['3D', '6D', '7H', 'QD', 'QS'])
# scoreRound(['2H', '2D', '4C', '4D', '4S'], ['3C', '3D', '3S', '9S', '9D'])
# print(scores)

with open("problem_54_text.txt", "r") as f:
    rounds = f.readlines()
    rounds = [x.strip("\n") for x in rounds]
    rounds = [x.split(" ") for x in rounds]

for r in rounds:
    scoreRound(r[:5], r[5:])

print(scores)
    
