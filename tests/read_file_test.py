import pytest
from main import read_file


# Тести для методу read_file
@pytest.mark.parametrize("file_content", [
    (["This is a test.\n", "The cat is cute.\n", "The dog is friendly.\n", "Python is awesome.\n"]),
])
def test_read_file(input_file, file_content):
    assert read_file(input_file) == file_content
