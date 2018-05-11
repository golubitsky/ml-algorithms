import unittest
import pytest
from src import math


def test_log_base_2_for_entropy():
    assert math.log_base_2_for_entropy(0) == 0


@pytest.mark.parametrize("p,expected", [
    (0, 0),
    (0.5, 1),
    (1, 0),
])
def test_entropy(p, expected):
    assert math.entropy(p) == expected