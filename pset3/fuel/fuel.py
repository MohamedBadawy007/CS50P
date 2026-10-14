while True:

    fraction = input("Fraction: ")
    pos = fraction.find("/")

    try:
        x = int(fraction[0:pos])
        y = int(fraction[(pos+1):])

    except ValueError:
        print("Enter valid numbers.")

    else:

        if x > y:
            continue

        if x < 0:
            print("Enter valid numbers.")
            continue

        try:
            z = (x/y) * 100

        except ZeroDivisionError:
            print("Can not divide by zero.")

        else:
            if z <= 1:
                print("E")

            elif z >= 99:
                print("F")

            else:
                print(f"{round(z)}%")

            break



