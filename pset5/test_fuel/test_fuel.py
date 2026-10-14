import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ValueError):
        convert("-3/4")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(70) == "70%"
    assert gauge(99) == "F"
    assert gauge(99.5) == "F"
    assert gauge(100) == "F"
