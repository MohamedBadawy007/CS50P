from validator_collection import validators

def main():
    print(validate(input("What's your email address? ")))

def validate(e):
    try:
        validators.email(e)

    except ValueError:
        return "Invalid"

    else:
        return "Valid"


if __name__ == "__main__":
    main()

