import sys
import csv
from tabulate import tabulate

def main():

    if checkinput():
        converttotable()


def checkinput():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        open(f"{sys.argv[1]}")

    except FileNotFoundError:
        sys.exit("File does not exist")

    else:
        return True


def converttotable():

    with open(f"{sys.argv[1]}") as file:
        reader = csv.reader(file)
        table = tabulate(reader, headers = "firstrow", tablefmt="grid")

    print(table)

main()


