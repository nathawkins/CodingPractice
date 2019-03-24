def main():
    def is_triplet(a,b,c):
        if a**2 + b**2 == c**2:
            return True
        return False

    for b in range(1,500):
        a = int((1000*(b-500))/(b-1000))
        c = 1000-a-b
        if is_triplet(a,b,c) and a+b+c == 1000:
            print(a,b,c, a*b*c)

if __name__ == '__main__':
    main()
    
