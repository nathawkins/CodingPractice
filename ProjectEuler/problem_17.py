##Define dictionaries of needed prefix lengths, etc.
hundred = 7
thousand = 8
nums = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3}
teens = {11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6}
prefixes = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}

def getlength(num):
    ##Setup parameter to store length
    length = 0

    ##Check the digit in the thousandths place by dividing by 1000
    thousands = int(num/1000)
    length += nums.get(thousands, 0)
    if thousands != 0:
        length += 8

    ##Redefine the number in question based on thousandths adjustment
    num = num - thousands*1000
    ##Get the number in the hundreds place by dividing by 100 and making an int
    hunds = int(num/100)
    length += nums.get(hunds, 0)
    ##If there is something in the hundreds place, add the prefix
    if hunds != 0:
        length += hundred

    ##Calculate the remainder based on subtracting the amount of hundreds
    remainder = num - hunds*100

    ##If there is a need for it, add the length of "and" in there
    if hunds != 0 and remainder != 0:
        length += 3 ##"and"

    ##If the remainder is less than 20, then directly give its lengths
    ##with no manipulation. These are the special cases
    if remainder <= 20 and remainder >= 11:
        length += teens.get(remainder, 0)
    ##Below ten just has the ones place
    if remainder <= 10:
        length += nums.get(remainder, 0)

    ##Else
    if remainder > 20:
        ##Find the tens digit by the same trick as the hundreds
        tens = int(remainder/10)
        length += prefixes.get(tens,0)

        ##Find the ones digit by subtracting away the tens
        ones = remainder - tens*10
        if ones == 0:
            length += 0
        else:
            length += nums.get(ones, 0)

    return length


total_length = 0
for i in range(1, 1001):
    total_length += getlength(i)
print(total_length)
