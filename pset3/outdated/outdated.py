months = {

    "January":"1",
    "February":"2",
    "March":"3",
    "April":"4",
    "May":"5",
    "June":"6",
    "July":"7",
    "August":"8",
    "September":"9",
    "October":"10",
    "November":"11",
    "December":"12"
}

while True:

    date = input("Date: ")

    if "/" in date:

        splitted = date.split("/")

        try:
            month = int(splitted[0])

        except:
            continue

        else:
            day = int(splitted[1])

            if not 1<=month<=12:
                continue
            if not 1<=day<=31:
                continue

            year = int(splitted[2])

            print(f"{year}-{month:02}-{day:02}")
            break

    else:

        try:
            for eachmonth in months:

                if eachmonth in date:
                    poscomma = date.find(",")
                    posspace = date.find(" ")

                    year = int(date[-4:])
                    day = int(date[posspace+1:poscomma])
                    month = int(months[eachmonth])

        except:
            continue

        else:

           if not 1<=day<=31:
               continue

           print(f"{year}-{month:02}-{day:02}", sep="",)
        break
