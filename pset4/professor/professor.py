import random

def main():

    level = get_level()

    count = 0

    for _ in range(10):

        chances = 0

        x = generate_integer(level)
        y = generate_integer(level)

        while True:
            try:
                answer = int(input(f"{x} + {y} = "))

            except ValueError:
                print("EEE")
                chances += 1

                if chances < 3:
                    continue
                else:
                    print(f"{x} + {y} = {x + y}")
                    break

            else:
                if answer != x + y:
                    print("EEE")
                    chances += 1

                    if chances < 3:
                        continue

                    else:
                        print(f"{x} + {y} = {x + y}")
                        chances = 0
                        break

                else:
                    count += 1
                    break

    print(f"Score: {count}")



def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        else:
            if 1 <= n <= 3:
                return n
            else:
                continue


def generate_integer(level):

    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)



if __name__ == "__main__":
    main()
