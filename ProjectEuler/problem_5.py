def main():
    found = False
    num = 2520
    check = [k for k in range(1,21)]
    while found == False:
        if all(num%i==0 for i in check):
            print("Solution found, smallest number divisible by 1 -> 20 is {}".format(num))
            found = True
            break
        else:
            num += 2520

if __name__ == '__main__':
    main()
