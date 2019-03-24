def main():
    with open("problem_65-text.txt") as textFile:
            rows = [row.split() for row in textFile]
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            rows[i][j] = int(rows[i][j])
    rows = rows[::-1]

    for i in range(len(rows)-1):
        this_row = rows[i]
        next_row = rows[i+1]
        for j in range(len(next_row)):
            next_value = next_row[j]
            this_value_1 = this_row[j]
            this_value_2 = this_row[j+1]
            if (next_value + this_value_1) > (next_value + this_value_2):
                next_row[j] = (next_value + this_value_1)
            else:
                next_row[j] = (next_value + this_value_2)

    # for row in rows:
    #     print(row)

    print(rows[-1][0])

if __name__ == '__main__':
    main()
