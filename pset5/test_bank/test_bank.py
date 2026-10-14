from bank import value

def test_hello_value():
    assert value("hello!") == 0
    assert value("hello, Mohamed") == 0
    assert value("Hello, Ali") == 0


def test_h_value():
    assert value("hey!") == 20
    assert value("hi, Mohamed") == 20
    assert value("Hi there!") == 20


def test_other_value():
    assert value("Good morning!") == 100
    assert value("Good evening") == 100
    assert value("Morning!") == 100


