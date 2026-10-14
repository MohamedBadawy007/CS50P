import csv
import sys


def main():
    if checkinput():
        convert()


def checkinput():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file")

    try:
        open(f"{sys.argv[1]}")

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    else:
        return True


def convert():

    with open(sys.argv[1]) as inputfile, open(sys.argv[2], "w") as outputfile:
        reader = csv.DictReader(inputfile)
        writer = csv.DictWriter(outputfile, fieldnames = ["first", "last", "house"])

        writer.writeheader()

        for eachdict in reader:
            fullname = eachdict["name"].split(", ")
            firstname = fullname[-1]
            lastname = fullname[0]
            place = eachdict["house"]
            writer.writerow({"first": firstname, "last": lastname, "house": place})


main()

