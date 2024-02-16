from twttr import shorten

def main():
    test_vowels()
    test_nonvowels()
    print("Output: ", result)

def test_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
def test_nonvowels():
    assert shorten("0123456789") == "0123456789"
    assert shorten("!@#$%^&")    == "!@#$%^&"

if __name__ == "__main__":
    main()
