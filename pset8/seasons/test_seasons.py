import pytest
from seasons import validate
import sys


def test_validate():
    assert validate("2020-02-02") == True
    with pytest.raises(SystemExit):
        validate("February 6th, 1998")

