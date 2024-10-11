import pytest
from main import is_palindrome

def simple_test_is_palindrome():
    assert is_palindrome('madam') == True
    assert is_palindrome('hello') == False


@pytest.mark.parametrize("test_input,expected", [
    ('level', True),
    ('python', False),
    ('racecar', True),
    ('', True),
])
def test_is_palindrome(test_input, expected):
    assert is_palindrome(test_input) == expected
