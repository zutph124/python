'''
In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house,
and the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

Converts that input to that output, splitting each name into a first name and last name.
Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments,
or if the first cannot be read, the program should exit via sys.exit with an error message.
'''

#
import sys
import csv
#
# main function
#
def main():
    output = []                       # list file

    try:
        infile = open(sys.argv[1],'r')
        readIt = csv.DictReader(infile)

        for row in readIt:
            splitName = row["name"].split(",")
            output.append({'first': splitName[1].strip(),
                            'last': splitName[0],
                            'house': row['house'],
                          })

        outfile = open(sys.argv[2],'w')
        writeIt = csv.DictWriter(outfile, fieldnames=['first', 'last', 'house'])
        writeIt.writerow({'first': "first", 'last': "last", 'house': "house"})
        for row in output:
            writeIt.writerow({'first': row["first"],
                              'last': row["last"],
                              'house': row["house"],
                             })
        infile.close()
        outfile.close()

    except FileNotFoundError:
        sys.exit("Could not read "+sys.argv[1])
        #sys.exit(f"Could not read {sys.argv[1]}")

#
# function to check arguments
#
def arguments():

    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__=="__main__":
    arguments()
    main()
