def main():
    two_before = 1
    one_before = 2
    series_terms = [1,2]

    this_term = 0
    while this_term < 4000000:
        this_term = two_before + one_before
        two_before = one_before
        one_before = this_term
        series_terms.append(this_term)

    even_tot = 0
    for term in series_terms:
        if term%2 == 0:
            even_tot += term

    print("The sum of even Fibanocci terms beflow 4 million is: {}".format(even_tot))

if __name__ == "__main__":
    main()
