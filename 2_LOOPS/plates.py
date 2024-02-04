##
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# All vanity plates must start with at least two letters.”
# vanity plates may contain a max of 6 chars (letters or numbers) and a min of 2 chars
# No periods, spaces, or punctuation marks are allowed.


def is_valid(s):
    if s[0:2].isalpha() and (len(s) >= 2 and len(s) < 7) and s.isalnum():
        #print(s.isalpha())
        counter  = 0
        firstnum = 0
        for n in s:
            if n.isnumeric():
                if firstnum == 0:
                    firstnum = 1
                    if int(n) != 0:                  # The first number used cannot be a ‘0’.”
                        if s[counter:].isnumeric():  # nrs cannot be used in the middle of a plate; they must come at the end.
                            #print("counter is ", counter)
                            #print(s[counter:])
                            return True
            counter += 1
        if s.isalpha():
            return True

main()
