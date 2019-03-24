# days_of_the_week = ["M", "T", "W", "R", "F", "S", "Sun"]
months = {"January":31, "February":28, "March":31, "April":30, "May":31, "June":30, "July":31, "August":31, "September":30, "October":31, "November":30, "December":31}

month_list = ["January","February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


year = 1901 ##Start in 1901
day = 1     ##Start on Tuesday

sundays = 0

while year < 2001:
    for m in range(12):
        ##How many days are in the month
        days_of_the_month = months.get(month_list[m], False)

        ##Handles the Leap Year
        if m == 1: ##If February
            ##Years
            if year%4 == 0 and year%400 !=0:
                days_of_the_month += 1
            ##Centuries
            elif year%4 == 0 and year%400 ==0:
                days_of_the_month += 1
            ##Something else
            else:
                pass

        ##What's the new day of the week?
        change_in_week = days_of_the_month%7

        day += change_in_week
        ##If we move to the next week
        if day >= 7:
            day -= 7

        ##Count only the sundays
        if day == 6:
            sundays +=1

    ##Move on to the next year!
    year += 1

print(sundays)
