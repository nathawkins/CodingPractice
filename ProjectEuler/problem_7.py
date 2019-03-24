def main(max):
    p_number = []
    num = 0
    while len(p_number)-1 < max:
        num += 1
        if all(num%i for i in range(2,int(num**(1/2))+1)):
            p_number.append(num)

    print(p_number[-1])

if __name__ == '__main__':
    main(10001)
