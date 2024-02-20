Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including lstrip and startswith.
Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
You might find it helpful to test your program on, e.g., some of Week 6’s source code as well as on programs of your own.

Recall that the csv module comes with quite a few methods, per docs.python.org/3/library/csv.html, among which are reader, per docs.python.org/3/library/csv.html#csv.reader, and DictReader, per docs.python.org/3/library/csv.html#csv.DictReader.
Note that the tabulate package comes with just one function, per pypi.org/project/tabulate. You can install the package with:
  pip install tabulate

Note that csv module comes with quite a few methods, per docs.python.org/3/library/csv.html, among which are DictReader, per docs.python.org/3/library/csv.html#csv.DictReader and DictWriter, per docs.python.org/3/library/csv.html#csv.DictWriter.
Note that you can tell a DictWriter to write its fieldnames to a file using writeheader with no arguments, per docs.python.org/3/library/csv.html#csv.DictWriter.writeheader.

Note that you can determine a file’s extension with os.path.splitext, per docs.python.org/3/library/os.path.html#os.path.splitext.
Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.

Note that the Pillow package comes with quite a few classes and methods, per pypi.org/project/Pillow. You might find its handbook and reference helpful to skim. You can install the package with:
  pip install Pillow
You can open an image (e.g., shirt.png) with code like:
  shirt = Image.open("shirt.png")
You can get the width and height, respectively, of that image as a tuple with code like:
  size = shirt.size
And you can overlay that image on top of another (e.g., photo) with code like
  photo.paste(shirt, shirt)
wherein the first shirt represents the image to overlay and the second shirt represents a “mask” indicating which pixels in photo to update.

Note that you can open an image (e.g., shirt.png) in VS Code by running
  code shirt.png
or by double-clicking its icon in VS Code’s file explorer.
