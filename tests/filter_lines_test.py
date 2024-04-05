import pytest
from main import filter_lines


# Тести для методу filter_lines
@pytest.mark.parametrize("lines, keyword, expected", [
    (["This is a test.", "The cat is cute.", "The dog is friendly.", "Python is awesome."], "dog",
     ["The dog is friendly."]),
    (["apple", "banana", "cherry", "date"], "a", ["apple", "banana", "date"]),
])
def test_filter_lines(lines, keyword, expected):
    assert filter_lines(lines, keyword) == expected


