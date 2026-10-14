# start with at least two letters
# no. characters from 2 to 6
# first no. can not be zero
# nos. must be last not in the middle of letters
# No periods, spaces, or punctuation marks are allowed.




def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    firsttwo = s[0:2]
    length = len(s)


    if not (firsttwo.isalpha() and 2 <= length <= 6 and s.isalnum()):
        return False

    for position, value in enumerate(s):

        if value.isdigit():
            if value == "0" and  s[position - 1].isalpha():
                return False

        if value.isalpha():
            if position != 0 and s[position - 1].isdigit():
                return False

    else:
        return True

if __name__ == "__main__":
    main()
