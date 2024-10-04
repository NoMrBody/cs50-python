import sys
import os
from PIL import Image
from PIL import ImageOps


def main():
    # print(sys.argv[0])
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line arguments")
    elif check_ext(sys.argv[1], sys.argv[2]) == False:
        sys.exit("Input and output have different extensions")
    else:
        try:
            photo = Image.open(sys.argv[1])
            pshirt = Image.open("shirt.png")
            photo = ImageOps.fit(photo, pshirt.size)
            photo.paste(pshirt, (0, 0), pshirt)
            photo.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("file not found")

def check_ext(file1, file2):
    ext1 = os.path.splitext(file1)[1]
    ext2 = os.path.splitext(file2)[1]
    return ext1 == ext2


if __name__ == "__main__":
    main()
