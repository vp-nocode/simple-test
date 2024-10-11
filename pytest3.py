import pytest
from main import sort_list

def test_sort1():
    assert sort_list([5, 6, 3, 1, 2]) == [1, 2, 3, 5, 6]
    assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]

@pytest.mark.parametrize("test_input,expected", [
    ([5, 6, 3, 1, 2], [1, 2, 3, 5, 6]),
    ([-1, 3, 0, -2, 2], [-2, -1, 0, 2, 3]),
    ([-1, 3, 0, -2, 2], [-1, 3, 0, -2, 2]),
    ('[]', []),
])
def test_sort_list(test_input, expected):
    assert sort_list(test_input) == expected
