import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    pattern = r'\bum\b'

    match = re.findall(pattern, s.lower().strip())

    return len(match)




if __name__ == "__main__":
    main()
