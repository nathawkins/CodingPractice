def main():
    ##Calculates the next triangle number in the series
    def triangle(n):
        return n*(n+1)/2

    def divisors(n):
        ##Keep track of the number of factors
        number_of_factors = 0

        ##For all of the integers between 1 and the sqrt() rounded up
        for i in range(1, int(1+((n)**(1/2)))+1):
            ##If the number is divisible by i, then add two factors
            ##one for n/i and the other for
            if n % i == 0:
                number_of_factors +=2
            if i*i==n:
                number_of_factors -=1
        return number_of_factors

##Finding how many divisors there are for each of the triangular numbers
    for n in range(1,1000000):
        Tn=triangle(n)
        if n%2==0:
            cnt=divisors(n/2)*divisors(n+1)
        else:
            cnt=divisors(n)*divisors((n+1)/2)
        if cnt >= 500:
            print(n)
            print(Tn)
            break

if __name__ == '__main__':
    main()
