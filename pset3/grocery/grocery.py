grocerylist = []

while True:

    try:
        item = input().upper()

    except EOFError:

        for eachitem in grocerylist:
            count = grocerylist.count(eachitem)
            if count > 1:
                for _ in range(count-1):
                    grocerylist.remove(eachitem)
            print(f"{count} {eachitem}", sep="")

        break

    else:

        grocerylist.append(item)

        grocerylist.sort()



