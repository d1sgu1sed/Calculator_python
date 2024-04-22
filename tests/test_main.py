import pytest
from src.main import (plus, division, minus, multi)

@pytest.fixture
def calcs_data():
    return [(1, 2, 3), (1, 2, 0.5), (3, 4, -1), (5, 2, 10)]

@pytest.fixture
def all_funcs():
    return [plus, division, minus, multi]

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)

def test_funcs(all_funcs, calcs_data):
    for method, (a, b, result) in zip(all_funcs, calcs_data):
        assert method(a, b) == result