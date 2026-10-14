# start with at least two letters
# no. characters from 2 to 6
# first no. can not be zero
# nos. must be last not in the middle of letters
# No periods, spaces, or punctuation marks are allowed.

from plates import is_valid

def test_twoletters():
    assert is_valid("55") == False
    assert is_valid("H") == False
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("USSR") == True
    assert is_valid("50CS") == False
    assert is_valid("C50S") == False
    assert is_valid("5C0S") == False


def test_nochar():
    assert is_valid("C") == False
    assert is_valid("USSRNAVY") == False
    assert is_valid("5") == False
    assert is_valid("DAVIDMALANISTHEBEST") == False
    assert is_valid("HEYTHERE50") == False

def test_firstzero():
    assert is_valid("CS500") == True
    assert is_valid("CS05") == False
    assert is_valid("05") == False
    assert is_valid("RTX070") == False
    assert is_valid("USS0") == False

def test_poschar():
    assert is_valid("CS5C0") == False
    assert is_valid("USS5R") == False
    assert is_valid("CS50P") == False

def test_punct():
    assert is_valid("CS50.1") == False
    assert is_valid("PI3.14") == False
    assert is_valid("HI,ALI") == False



