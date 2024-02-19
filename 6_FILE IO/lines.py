#
# In a file called lines.py, implement a program that expects exactly one command-line argument, 
# the name (or path) of a Python file, and outputs the number of lines of code in that file, 
# excluding comments and blank lines. 

# If the user does not specify exactly one command-line argument, 
# or if the specified file’s name does not end in .py, 
# or if the specified file does not exist, 
# the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment. 
# (A docstring should not be considered a comment.) 
# Assume that any line that only contains whitespace is blank.
#


import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

count = 0

try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.lstrip().startswith("#"): continue    # ignore comments
            ####if line == '\n':  continue        # ignore "new line" character
            if line.isspace():    continue        # remove blank lines
            count = count + 1
            ####print(line.rstrip())              # remove EOL code
        print(count)

except FileNotFoundError:
    sys.exit("File does not exist")
