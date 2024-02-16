'''
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2,
restructuring your code per the below, wherein shorten expects a str as input and
returns that same str but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.

    def main():
        ...

    def shorten(word):
        ...

    if __name__ == "__main__":
        main()

Then, in a file called test_twttr.py, implement one or more functions that collectively
test your implementation of shorten thoroughly, each of whose names should begin with test_
so that you can execute your tests with:

    pytest test_twttr.py

'''


def main():
   str = input("Input : ")
   shorten(str)
   print("Output: ", result)

def shorten(word):

#   20240214                                      remove UPPERCASE to make test.python.py show failures
    vowels = ['a', 'e', 'i', 'o', 'u']            #, 'A', 'E', 'I', 'O', 'U']
    global result
    result = ""

    for i in range(len(word)):
        if word[i] not in vowels:
            result = result + word[i]
    return result

if __name__ == "__main__":
    main()
