from bank import value

def main():
    test_hello()
    test_h()
    test_other()
    print(v)

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
def test_h():
    assert value("hi")    == 20
    assert value("HI")    == 20
def test_other():
    assert value("0123456789") == 100

if __name__ == "__main__":
    main()
