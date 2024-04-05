import pytest
from main import write_file


# Тести для методу write_file
@pytest.mark.parametrize("output_file, lines, expected", [
    ("test_output.txt", ["The cat is cute.", "The dog is friendly."], ["The cat is cute.The dog is friendly."]),
])
def test_write_file(tmp_path, output_file, lines, expected):
    file_path = tmp_path.joinpath(output_file)
    write_file(str(file_path), lines)
    with open(file_path, 'r') as file:
        assert file.readlines() == expected
