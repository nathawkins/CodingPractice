def stringWithEnumeration(string):
    '''
    Ex: 
    >>> stringWithEnumeration("AAABBCDAA")
    "3A2B1C1D2A"
    '''

    result = ""
    current_letter = ""
    count = 0
    for letter in string:
        if current_letter == "":
            current_letter = letter
            count += 1
        elif current_letter == letter:
            count += 1
        else:
            result += str(count)
            count = 0
            result += current_letter
            current_letter = letter
            count += 1

    result += str(count)
    result += current_letter

    return result