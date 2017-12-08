def main():
    number = 600851475143

    largest_factor = 1

    def isPrime(num):
        return all(num % i for i in range(2, num))

    for factor in range(10000000):
        if factor == 0:
            continue
        if number%factor == 0:
            if isPrime(factor):
                if factor > largest_factor:
                    largest_factor = factor

    print("The largest prime factor of {} is {}.".format(number, largest_factor))

if __name__ == "__main__":
    main()
