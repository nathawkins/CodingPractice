def main():
    ##Create a dictionary to hold previous solutions
    known = {}

    max_length = 0
    num = 0

    lim = 1000000
    for trial in range(1,lim+1):
        ##What number are we looking at now?
        n = trial
        ##Keep track of the terms in the series
        count = 0
        ##End when number is 1 (terminates there)
        while n != 1:
            count += 1

            ##Do the division for even terms
            if n%2 == 0:
                n /= 2
                ##Check against previous solutions. If we have solved this one before
                ##just add its series length to the count and move on
                if known.get(n, False) != False:
                    count+= known.get(n, "")
                    break
                else:
                    count += 0

            ##Do the same for odd terms
            else:
                n = 3*n+1
                if known.get(n, False) != False:
                    count+= known.get(n, "")
                    break
                else:
                    count += 0

        ##Add this to the dictionary. The length for the series of this number. Continually doing
        ##this reduces the number of iterations needed in the while loop over time because
        ##we have solved more and more series.
        known[trial] = count

        if  count > max_length:
            max_length = count
            num = trial

    print("Longest Collatz Length: {}. Number: {}.".format(max_length, num))

if __name__ == '__main__':
    main()
