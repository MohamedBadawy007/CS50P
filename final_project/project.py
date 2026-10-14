class Item:

    def __init__(self, num, name, unit_type, unit_price, quant_or_am=0):
        self.num = num
        self.name = name
        self.unit_type = unit_type
        self.unit_price = unit_price
        self.quant_or_am = quant_or_am

    def __str__(self):
        return f"#{self.num} {self.name} price: {self.unit_price}EGP{self.unit_type}"


class Cart:

    def __init__(self):
        self.items = []

    def calc_total(self):
        total = []
        for each in self.items:
            total.append(each.unit_price * each.quant_or_am)
        return f"Total = {sum(total):.2f}EGP"

    def __str__(self):
        details = ""
        for each in self.items:
            details += f"|{each.name}: {each.quant_or_am}x{each.unit_price}EGP|\n"

        return f"""
{details}
{self.calc_total()}
        """


milk = Item(1, "Milk Bottles (1L)", "/bottle", 60)
cheddar = Item(2, "Cheddar Cheese", "/1000gm", 800)
eggs = Item(3, "Eggs", "/egg", 5)
meat = Item(4, "Meat", "/1000gm", 500)
juice = Item(5, "Juice Bottles (1L)", "/bottle", 50)
water = Item(6, "Water Bottles (0.6L)", "/bottle", 10)
oil = Item(7, "Oil Bottles (1.6L)", "/bottle", 170)
sugar = Item(8, "Sugar Packets", "/packet", 30)
bread = Item(9, "Bread Loaves", "/loaf", 2)


cart = Cart()


menu = [milk, cheddar, eggs, meat, juice, water, oil, sugar, bread]


def main():
    print("Hello, how can I help you?")

    while True:
        n_feature = show_features()

        match n_feature:

            case 1:
                while True:
                    n_to_add = show_add_case()
                    if n_to_add == 0:
                        break
                    else:
                        if add_to_cart(n_to_add) == "Error":
                            continue
                        display_cart()

            case 2:
                if cart.items == []:
                    print("Cannot remove an item from an empty cart!")
                    continue
                else:
                    while True:
                        if cart.items == []:
                            break
                        n_to_remove = show_remove_case()
                        if n_to_remove == 0:
                            break
                        remove_from_cart(n_to_remove)
                        continue

            case 3:
                if cart.items == []:
                    print("Cannot edit any item in an empty cart!")
                    continue
                else:
                    while True:
                        n = show_edit_case()
                        if n == 0:
                            break
                        edit(n)
                        continue

            case 4:
                cart.items.clear()
                print("Thanks for your time reviewing our products!")
                exit()

            case 5:
                display_cart()
                print("Thanks for buying from us!")
                exit()


def display_features():
    return f"""
Choose a number from the features menu!
#{1} Add to the Cart
#{2} Remove an Item from the Cart
#{3} Edit an Item's Quantity
#{4} Empty the Cart and Exit
#{5} Check Out
        """


def show_features():
    while True:
        try:
            print(display_features())
            n_feature = int(input("Feature number: "))
        except ValueError:
            print("Enter a valid number!")
            continue
        else:
            if n_feature not in [1, 2, 3, 4, 5]:
                print("Choose a number from the list!", "\n")
                continue
            print()
            return n_feature


def display_cart():
    print(cart)


def show_add_case():
    print("Choose an item to add to your cart!", "\n")
    for each in menu:
        print(each)
    print()
    print(f"press {0} to go back")
    while True:
        try:
            n = int(input("Item number: "))
        except ValueError:
            print("Enter a valid number!")
            continue
        else:
            if not 0 <= n <= len(menu):
                print("Choose a number from the list!")
                continue
            print()
            return n


def add_to_cart(n_to_add):
    if menu[n_to_add - 1] in cart.items:
        print("""
Can't add an already-existing item!
Return back to the features menu using '0' to edit it's quantity, remove it or checkout.
            """)
        return "Error"
    if menu[n_to_add - 1].unit_type == "/1000gm":
        print("How much do you want?")
        while True:
            try:
                amount = int(input("Amount in grams: "))
            except ValueError:
                print("Enter a valid number!")
                continue
            else:
                if not 0 < amount:
                    print("Enter a valid amount!")
                    continue
                menu[n_to_add - 1].quant_or_am = float(amount) / 1000
                cart.items.append(menu[n_to_add - 1])
                break

    else:
        print("How many do you want? ")
        while True:
            try:
                q = int(input("number: "))
            except ValueError:
                print("Enter a valid number!")
                continue
            else:
                if not 0 < q:
                    print("Enter a valid number!")
                    continue
                menu[n_to_add - 1].quant_or_am = q
                cart.items.append(menu[n_to_add - 1])
                break


def show_remove_case():
    print("Select an item to remove", "\n")
    for i, each in enumerate(cart.items):
        print(f"#{i+1} {each.name}")
    print()
    print(f"press {0} to go back")
    while True:
        try:
            n_to_remove = int(input("number: "))
        except ValueError:
            print("Enter a valid number!")
            continue
        else:
            if not 0 <= n_to_remove <= len(cart.items):
                print("Choose a number from the list!")
                continue
            print()
        return n_to_remove


def remove_from_cart(n_to_remove):
    del cart.items[n_to_remove - 1]
    print()
    display_cart()


def show_edit_case():
    print("Select an item to edit", "\n")
    for i, each in enumerate(cart.items):
        print(f"#{i+1} {each.name}")
    print()
    print(f"press {0} to go back")
    while True:
        try:
            n = int(input("number: "))
        except ValueError:
            print("Enter a valid number!")
            continue
        else:
            if not 0 <= n <= len(cart.items):
                print("Choose a number from the list!")
                continue
            print()
            return n


def edit(n):
    if cart.items[n - 1].unit_type == "/1000gm":
        print(f"Current amount: {cart.items[n-1].quant_or_am * 1000} grams")
        while True:
            try:
                new = int(input("Enter desired amount: "))
            except ValueError:
                print("Enter valid amount!")
                continue
            else:
                if not 0 < new:
                    print("Enter valid amount!")
                    continue
                cart.items[n - 1].quant_or_am = new / 1000
                display_cart()
                break
    else:
        print(f"Current number: {cart.items[n-1].quant_or_am} units")
        while True:
            try:
                new = int(input("Enter desired number: "))
            except ValueError:
                print("Enter valid number!")
                continue
            else:
                if not 0 < new:
                    print("Enter valid number!")
                    continue
                cart.items[n - 1].quant_or_am = new
                display_cart()
                break


if __name__ == "__main__":
    main()
