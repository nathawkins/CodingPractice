def verifyParenthesesString(myStr: str) -> bool:
    '''
    Function to check a series of parentheses and conclude
    whether or not it is 'complete.'

    For example: "[()()]{[]}" would return True
    because each pair of parentheses has both an opening
    and closing bracket and are ordered in such a way that there
    is no overlap or misordering

    "([)]" would return False because each parenthese has 
    an open and close, but a closing parenthese for one type of
    parenthese interrupts the closing parenthese of a square bracket
    '''

    openings = ["{", "[", "("]
    closings = ["}", "]", ")"]

    stack= []
    for i in myStr:
        if i in openings:
            print(i, "Opening", stack)
            stack.append(i)
        elif i in closings:
            pos = closings.index(i)
            print(i, "Closing", pos, stack)
            if ((len(stack) > 0) and (openings[pos] == stack[len(stack)-1])):
                print("Closing parentheses found", stack)
                stack.pop()
                print("Opening parentheses removed", stack)
            else:
                return False
    if len(stack) == 0:
        return True


print(verifyParenthesesString("[(){()}]"))