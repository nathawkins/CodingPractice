def main():
    def is_palindrome(number):
        str_num = str(number)
        bits = list(str_num)
        if bits == bits[::-1]:
            return True
        else:
            return False

    largest = 0

    for k in range(101,1000):
        for j in range(101, 1000):
            if is_palindrome(k*j) and (k*j) > largest:
                largest = k*j

    print("The largest palindrome number made by multiply two three digit numbers is {}".format(largest))

if __name__ == '__main__':
    main()
