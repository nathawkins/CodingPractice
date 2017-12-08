def main():
    sq_sum = sum([i**2 for i in range(1,101)])
    sum_sq = (sum([i for i in range(1,101)]))**2
    print("Square of sum minus sum of squares is equal to {}".format(sum_sq-sq_sum))
    
if __name__ == '__main__':
    main()
