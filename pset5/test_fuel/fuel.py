def main():
    string = input("Fraction: ")
    per = convert(string)
    gauge(per)


def convert(fraction):
    fraction = str(fraction)
    pos = int(fraction.find("/"))

    try:
        x = int(fraction[:pos])
        y = int(fraction[(pos+1):])

        if (x > y and y != 0):
            raise ValueError

        if x < 0 or y < 0:
            raise ValueError

        if y == 0:
            raise ZeroDivisionError

    except ValueError:
        raise ValueError

    else:
        z = (x/y) * 100
        return round(z)



def gauge(percentage):
    percentage = int(percentage)

    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
