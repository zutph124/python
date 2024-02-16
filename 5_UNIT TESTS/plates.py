'''
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below,
wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not,
but main is only called if the value of __name__ is "__main__":

        def main():
            ...


        def is_valid(s):
            ...


        if __name__ == "__main__":
            main()

Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation
of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

        pytest test_plates.py
'''


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("InValid")

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

if __name__ == "__main__":
    main()
