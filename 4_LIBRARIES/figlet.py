'''
In a file called figlet.py, implement a program that:
- Expects zero or two command-line arguments:
  . Zero if the user would like to output text in a random font.
  . Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, 
    and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, 
the program should exit via sys.exit with an error message.
'''


from pyfiglet import Figlet
import random
import sys               # Command-Line Arguments

figlet = Figlet()
font = figlet.getFonts()
##print(font)                          debugger
##print(len(sys.argv))                 debugger  
##print("sys_argv_0", sys.argv[0])     debugger 
##print("sys_argv_1", sys.argv[1])     debugger 
##print("sys_argv_2", sys.argv[2])     debugger 

if   len(sys.argv) == 1:
    figlet.setFont(font=random.choice(font))

elif len(sys.argv) == 3:
    if (sys.argv[1]) not in ['-f','--font']:
        sys.exit("Error msg1: incorrect parm,  -f / --font not found")

    if (sys.argv[2]) not in font:
        sys.exit("Error msg2: specified font not found in font library")

    figlet.setFont(font=sys.argv[2])

else:
    sys.exit("Error msg3: incorrect input")

str = input("Input: ")
print(figlet.renderText(str))
