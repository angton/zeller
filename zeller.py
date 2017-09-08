def checkYear():
    while True:
        try:
            global year
            #gör variabeln year global = möjlig att nå i andra funktioner
            year = int(input('Year: '))
            #frågar efter input
        except ValueError:
            print('Please insert numbers only')
            continue
        #kollar om input är en int (behövs egentligen inte enligt instruktioner)

        if year not in range(1583, 10000):
            print('Out of allowed range 1583 - 9999')
        else:
            return year
        #kollar om year är i rangen 1583 - 9999

def checkMonth():
    while True:
        try:
            global month
            #gör variabeln year global = möjlig att nå i andra funktioner
            month = int(input('Month: '))
            #frågar efter input
        except ValueError:
            print('Please insert numbers only')
            continue
        #kollar om input är en int (behövs egentligen inte enligt instruktioner)

        if month not in range(1, 13):
            print('Out of allowed range 1 - 12')
        else:
            return month
        #kollar om month är i rangen 1 - 12

def checkDay():
    while True:
        try:
            global day
            #gör variabeln year global = möjlig att nå i andra funktioner
            day = int(input('Day: '))
            #frågar efter input
        except ValueError:
            print('Please insert numbers only')
            continue
        #kollar om input är en int (behövs egentligen inte enligt instruktioner)

        if month in {1, 3, 5, 7, 8, 10, 12}:
        #kollar efter antalet dagar i angiven månad
            if day not in range(1, 32):
                print('Out of allowed range 1 - 31')
            else:
                return day

        if month in {4, 6, 9, 11}:
        #kollar efter antalet dagar i angiven månad
            if day not in range(1, 31):
                print('Out of allowed range 1 - 30')
            else:
                return day

        if month == 2:
        #kollar efter antalet dagar i februari
            if year % 4 == 0 and year % 100 != 0:
            #skottår!
                if day not in range(1, 29):
                    print('Out of allowed range 1 - 28')
                else:
                    return day
            else:
            #inte skottår!
                if day not in range(1, 30):
                    print('Out of allowed range 1 - 29')
                else:
                    return day

def getWeekday():
    global month
    global year
    #behövs för att komma åt och override:a variablerna (bör skrivas på annat sätt, tex parametrar)

    if month == 1 or month == 2:
        month += 12
        year -= 1
    #gör om januari och februari enligt instruktionerna

    weekday = (day + 13*(month + 1)//5 + year + year//4 - year//100 + year//400 ) % 7
    #Zellers kongruensformel

    if weekday == 0:
        print('It is a saturday')
    elif weekday == 1:
        print('It is a sunday')
    elif weekday == 2:
        print('It is a monday')
    elif weekday == 3:
        print('It is a tuesday')
    elif weekday == 4:
        print('It is a wednesday')
    elif weekday == 5:
        print('It is a thursday')
    elif weekday == 6:
        print('It is a friday')
    else:
        return

if __name__ == '__main__':
#main-metoden som exekverar funktionerna i tur och ordning
    checkYear()
    checkMonth()
    checkDay()
    getWeekday()


