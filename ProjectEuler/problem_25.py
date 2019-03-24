##Define the first two terms in the fibonacci sequence
fibs = [1,1]

##Define a function that calls the global list of numbers and calculates the
##next fibonacci number. Also stores the value.
def fibonacci(ind):
    global fibs
    a = fibs[ind-2] + fibs[ind-3]
    fibs.append(a)
    return a

##What's the maximum number of digits we want in the fibonacci number
threshold = 1000

for k in range(3,10000):
    ##Calculate the number, break it into digits in a list. Find the length.
    digits = list(str(fibonacci(k)))
    ##If we hit 1000, break
    if len(digits) == threshold:
        ##Give index result
        print("Threshold of {} digits reached. Index: {}".format(threshold,k))
        print("Fibonacci number: {}".format(fibonacci(k)))
        break
