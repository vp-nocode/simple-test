import pytest
from at02 import count_vowel


@pytest.mark.parametrize("test_input,expected", [
    ('мама миа', 4),
    ('длиношеее животное', 9),
    ('', 0),
    ('срспск', 0),
    ('banzai', 0),
])
def test_count_vowel(test_input, expected):
    assert count_vowel(test_input) == expected
