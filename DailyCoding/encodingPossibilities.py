'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded 
message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be 
decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, 
'001' is not allowed.
'''

string = "abcdefghijklmnopqrstuvwxyz"
encodingKey = {}

for i,s in enumerate(string):
    encodingKey[s] = i+1


def numToLetter(num_s):
    for s in list(encodingKey.keys()):
        if encodingKey[s] == int(num_s):
            return s

def decodeListNumStrings(str_l):
    res = ""
    for str_num in str_l:
        res = res + numToLetter(str_num)

    return res

def getAllEncodings(string):
    strings = [list(string)]
    
    for i in range(len(string)-1):
        this_string_l = []
        j = 0
        while j < i:
            this_string_l.append(string[j])
            j += 1
        this_string_l.append(string[i:i+2])
        j = i+2
        while j < len(string):
            this_string_l.append(string[j])
            j += 1

        strings.append(this_string_l)


    pairs_end = [string[i]+string[i+1] for i in range(0, len(string)-1, 2)]
    if len(string) % 2 != 0:
        pairs_end = pairs_end + [string[-1]]
    pairs_start = [string[i]+string[i+1] for i in range(1, len(string)-1, 2)]
    if len(string) %2 != 0:
        pairs_start = [string[0]] + pairs_start

    strings.append(pairs_start)
    strings.append(pairs_end)


    return strings

def getAllAllowableEncodings(string):
    all_strings = getAllEncodings(string)

    allowable = []

    for l in all_strings:
        allgood = True
        for item in l:
            if int(item) > 26:
                allgood = False
        if allgood and len("".join(l)) == len(string):
            allowable.append(l)

    res = [decodeListNumStrings(x) for x in allowable]

    return list(set(res))

print(getAllAllowableEncodings('111'))
print(getAllAllowableEncodings('1112'))
print(getAllAllowableEncodings('1211'))
