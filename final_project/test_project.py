import pytest
from project import display_features, show_features, show_add_case


def test_display_features():
    assert display_features() == f'''
Choose a number from the features menu!
#{1} Add to the Cart
#{2} Remove an Item from the Cart
#{3} Edit an Item's Quantity
#{4} Empty the Cart and Exit
#{5} Check Out
        '''


def test_show_features(monkeypatch):

    answers = iter(["add", "20", "2"])
    monkeypatch.setattr("builtins.input", lambda fake_ns : next(answers))
    assert show_features() == 2


def test_show_add_case(monkeypatch):

    answers = iter(["milk", "55", "7"])
    monkeypatch.setattr("builtins.input", lambda fake_ns : next(answers))
    assert show_add_case() == 7
