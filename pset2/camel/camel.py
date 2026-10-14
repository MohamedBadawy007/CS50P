camelinput = input("camelCase: ")

letters = []

words = []

for eachletter in camelinput:

    if eachletter.islower():
        letters.append(eachletter)

    elif eachletter.isupper():
        newword = "".join(letters).lower()
        words.append(newword)
        letters.clear()
        letters.append(eachletter)

newword = "".join(letters).lower()
words.append(newword)



print("_".join(words))

