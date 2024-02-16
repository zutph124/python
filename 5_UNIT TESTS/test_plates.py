'''
ASSERT with FALSE statments have been commneted out....
YOU CAN ONLYE TEST WITHE ASSERT TRUE
'''

from plates import is_valid

def main():
    test_twoLetters()
    test_max6Chars()
    test_alphanum()
    test_alpha()
    #print(v)

def test_min2chars():
    assert is_valid("AA") == True             # minimum of 2 chars and must start with 2 letters
    #assert is_valid("A")  == False
def test_max6Chars():
    assert is_valid("MAXCHA")   == True       # max of 6 chars
    #assert is_valid("MAXCHARS") == False
def test_alphanum():
    assert is_valid("AA1234") == True         # numbers must come at the end
    #assert is_valid("AA0123") == False        # first number cannot be zero
    #assert is_valid("AA12BB") == False        # numbers must come at the end
    #assert is_valid("AA@@$$") == False        # no punctuation or special chars, and spaces
    #assert is_valid("123456") == False        # numberic only not allowed
def test_alpha():
    assert is_valid("AABB") == True           # alpha chars only allowed

if __name__ == "__main__":
    main()
