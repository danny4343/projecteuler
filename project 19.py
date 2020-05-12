def lp(n):
    if n%400==0:
        return(True)
    if n%100==0:
        return(False)
    else:
        if n%4==0:
            return(True)
        else:
            return(False)

counter=0
fday = 1

def main(y):
    global counter
    global fday
    year=y
    for x in range(12):
        day = fday
        if fday==6:
            counter+=1
        month = x
        if (month == 0) or (month == 2) or (month == 4) or (month==6) or (month==7) or (month==9) or (month==11):
            days=30
        else:
            if month == 1:
                if lp(year):
                    days=28
                else:
                    days=27
            else:
                days=29
        for z in range(days+1):
            if z!=days:
                if day==6:
                    day=0
                else:
                    day+=1
        if day == 6:
            fday = 0
        else:
            fday = day+1

for x in range(1901,2001):
    main(x)


print(counter)
