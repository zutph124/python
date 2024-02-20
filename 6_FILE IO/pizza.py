''' In a file called pizza.py, implement a program that expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate,
a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format.
If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .csv,
or if the specified file does not exist, the program should instead exit via sys.exit.
'''

#
# pip install tabulate done on 2023/02/10 and again on 2024/02/20
#

import sys

import csv

from tabulate import tabulate

#
# main function
#
def main():

    table = []
    try:
        with open(sys.argv[1], newline='') as csvfile:
            reader = csv.reader(csvfile)
            ####reader = csv.DictReader(csvfile)
            for row in reader:
                table.append(row)
            print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

#
# function to check arguments
#
def arguments():

    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
