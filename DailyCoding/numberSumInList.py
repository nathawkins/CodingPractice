'''
Given a list of numbers and a number k, 
return whether any two numbers from the 
list add up to k.

For example, given [10, 15, 3, 7] and k 
of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def sumInList(n_list, num):
    def extendList(n_list, repetitions):
        extended_list = []
        for N in n_list:
            for R in range(repetitions):
                extended_list.append(N)

        return extended_list

    for A,B in zip(len(n_list)*n_list, extendList(n_list, len(n_list))):
        print(A,B)
        if A+B == num:
            return True

    return False

print(sumInList([10,5,7,3], 17))
