import pytest
from um import count
'''
:) um.py yields 1 for "um"
:) um.py yields 1 for "Hello, um, world"
:) um.py yields 1 for "This is, um... CS50."
:) um.py yields 1 for "Um... what are regular expressions?"
:) um.py yields 2 for "Um, thanks, um, regular expressions make sense now."
:) um.py yields 2 for "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
'''

def test_word():
    assert count("um") == 1
    assert count("um, um") == 2
    assert count("um, um, um") == 3

def test_noword():
    assert count("") == 0
    assert count("Hi there!") == 0
    assert count("Hello!") == 0

def test_text():
    assert count("Hello, my name is...") == 0
    assert count("Yummy, that's very delicious!") == 0
    assert count("Hello, um, My name is...") == 1
    assert count("Hi, um, I'm Ali, um, would you like a coffee?") == 2
    assert count("Um, I'm, um, very frigthened, um") == 3
