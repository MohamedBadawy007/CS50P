import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

fontslist = figlet.getFonts()


def main():

    if len(sys.argv) == 1:
        s = input("Input: ")
        f = random.choice(fontslist)
        figlet.setFont(font=f)
        print(figlet.renderText(s))

    elif (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fontslist:
        s = input("Input: ")
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(s))

    else:
        sys.exit("Invalid usage")


main()
