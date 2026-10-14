print("Amount Due: 50")

allowedcoins = [25, 10, 5]

amountdue = 50

while True:

    coinspaid = int(input("Insert coin: "))

    if coinspaid in allowedcoins:


        amountdue = int(amountdue - coinspaid)

        if 0 < amountdue <= 50 :
            print(f"Amount Due: {amountdue}")

            continue

        elif amountdue == int(0):
            print("Change owed: 0")
            break

        elif amountdue < 0 :
            print(f"Change owed: {-amountdue}")
            break

    else:
        print(f"Amount Due: {amountdue}")
        continue


