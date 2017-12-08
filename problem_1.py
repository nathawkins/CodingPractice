def main():
    k = 1
    dk = 1
    total = 0
    while k < 1000:
        if k%3 ==0 or k%5==0:
            total += k
        k += dk
    print(total)

if __name__ == '__main__':
    main()
    
