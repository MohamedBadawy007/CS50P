import sys
from PIL import Image, ImageOps
from os import path


validexts = [".jpg", ".jpeg", ".png"]


def main():

    if checkinput():
        convert()

def checkinput():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not path.splitext(sys.argv[1])[1] in validexts:
        sys.exit("Invalid input")

    elif not path.splitext(sys.argv[2])[1] in validexts:
        sys.exit("Invalid output")

    if path.splitext(sys.argv[1])[1] != path.splitext(sys.argv[2])[1]:
        sys.exit("Input and output have different extensions")

    try:
        open(f"{sys.argv[1]}")

    except FileNotFoundError:
        sys.exit("Input does not exist")

    else:
        return True


def convert():

    with Image.open(sys.argv[1]) as img:

        with Image.open("shirt.png") as tshirt:

            img = ImageOps.fit(img, tshirt.size)

            img.paste(tshirt, tshirt)
            img.save(sys.argv[2])



main()
