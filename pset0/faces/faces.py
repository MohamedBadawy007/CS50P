def convert(text):
    text = text.replace(":(" , "🙁")
    return text.replace(":)" , "🙂")

def main():
    text = input()
    text = convert(text)
    print(text)

main()
