def main():
    def get_both(num):
        big_num = 2**(num)
        s_big = str(big_num)
        ls = list(s_big)
        total = 0
        for val in ls:
            total += int(val)
        return total

    print(get_both(1000))

if __name__ == '__main__':
    main()
    
