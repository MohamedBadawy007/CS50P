def main():

    actualtime = input("what time is it? ")

    actualusedtime = convert(actualtime)

    if 7.0 <= actualusedtime <= 8.0 :
        print("breakfast time")

    elif 12.0 <= actualusedtime <= 13.0 :
        print("lunch time")

    elif 18.0 <= actualusedtime <= 19.0 :
        print("dinner time")

    else:
        return

def convert(time):

    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes)

    minutes = minutes / 60

    time = hours + minutes

    time = float(time)

    return time


if __name__ == "__main__":
    main()














'''
def convert(generaltime):

    hours, minutes = generaltime.split(":")

    hours = float(hours)
    minutes = float(minutes)

    if 13.0 <= hours < 24.0  and hours != 19.0 :
        hours = hours - 12

    elif hours == 19.0:
        hours = 19.0

    else:
        hours = hours

    minutes = minutes / 60

    generaltime = hours + minutes

    generaltime = float(generaltime)

    return generaltime


def main():

    actualtime = input("what time is it? ")

    actualusedtime = convert(actualtime)

    if 7.0 <= actualusedtime <= 8.0 :
        print("breakfast time")

    elif 12.0 <= actualusedtime <= 1.0 :
        print("lunch time")

    elif 6.0 <= actualusedtime < 7.0 or actualusedtime == 19.0:
        print("dinner time")

    else:
        return

main()
'''
