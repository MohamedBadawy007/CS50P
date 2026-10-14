import random

def main():

    while True:
        try:
            n = int(input("Level: "))

            if n <= 0:
                continue

        except ValueError or TypeError:
            continue

        else:
            break

    randomnumber = random.randint(1, n)

    while True:
        try:
            guess = int(input("Guess: "))

            if guess <= 0:
                continue

        except ValueError:
            continue

        else:
            if guess < randomnumber:
                print("Too small!")
                continue
            elif guess > randomnumber:
                print("Too large!")
                continue
            elif guess == randomnumber:
                print("Just right!")
                exit()




main()
