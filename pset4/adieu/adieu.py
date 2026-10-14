import inflect

p = inflect.engine()

def main():

    nameslist = []

    try:
        while True:
            name = input("Name: ")
            nameslist.append(name)

    except EOFError:
        print()
        print(f"Adieu, adieu, to {p.join(nameslist)}")


main()
