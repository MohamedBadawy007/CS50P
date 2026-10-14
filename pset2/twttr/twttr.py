
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    for eachletter in word:

        if eachletter in vowels:
            word = word.replace(eachletter, '')

    return word


if __name__ == "__main__":
    main()
