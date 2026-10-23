import pytest
from q01 import ackermann


def test_base_cases():
    assert ackermann(0, 0) == 1
    assert ackermann(0, 5) == 6
    assert ackermann(1, 0) == 2
    assert ackermann(2, 0) == 3

def test_recursive_cases():
    assert ackermann(1, 1) == 3
    assert ackermann(2, 2) == 7
    assert ackermann(3, 2) == 29

def test_larger_values():
    # these are computationally intensive, so keep them small
    assert ackermann(3, 3) == 61
    assert ackermann(3, 4) == 125
    assert ackermann(3, 6) == 509
