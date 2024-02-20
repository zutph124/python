'''
In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input
after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open,
resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
using default values for method, bleed, and centering, overlay the shirt with Image.paste,
per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste,
and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

    if the user does not specify exactly two command-line arguments,
    if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    if the input’s name does not have the same extension as the output’s name, or
    if the specified input does not exist.
'''

#
import sys
from os.path import splitext

from PIL import Image, ImageOps
#
# main function
#
def main():

    try:
        im1 = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Input does not exist {sys.argv[1]}")

    shirt = Image.open("shirt.png")
    size = shirt.size
    im2 = ImageOps.fit(im1, size)
    im2.paste(shirt, shirt)
    im2.save(sys.argv[2])
#
# function to check arguments
#
# (1) must have 2 arguments
# (2) input and output must end in .jpg, .jpeg, .png
#
def arguments():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if file1[1] not in ['.jpg', '.jpeg', '.png']:
         sys.exit("Invalid input")

    if file2[1] not in ['.jpg', '.jpeg', '.png']:
         sys.exit("Invalid output")

    if file1[1] != file2[1]:
        sys.exit("Input and output have different extensions")

if __name__=="__main__":
    arguments()
    main()
