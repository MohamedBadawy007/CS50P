import sys
import re
from datetime import date
import inflect

p = inflect.engine()

def main():

    today_date = date.fromisoformat(str(get_today()))

    birthdate = input("Date of Birth: ")
    if validate(birthdate):
        birthdate = date.fromisoformat(birthdate)

        difference = calc_diff(today_date, birthdate)

        text = conv_num_to_words(difference)

        print(f"{text} minutes")


def get_today():
    return date.today()


def validate(birthdate):
    if not re.search(r"[0-9][0-9][0-9][0-9]-([0][1-9]|[1][0-2])-([0][1-9]|[1-2][0-9]|[3][0-1])", birthdate):
        sys.exit("Invalid date")
    else:
        return True


def calc_diff(a, b):
    diff = str(a - b)
    pos = diff.find(" ")
    return int(diff[:pos])*1440


def conv_num_to_words(n):
     return str(p.number_to_words(n)).replace(" and", "").capitalize()


if __name__ == "__main__":
    main()
