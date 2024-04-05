import pytest
from main import filter_file


# Тести для методу filter_file
@pytest.mark.parametrize("input_content, keyword, expected", [
    ("This is a test.\nThe cat is cute.\nThe dog is friendly.\nPython is awesome.\n", "cat",
     ["The cat is cute.\n"]),
    ("This is a test.\nThe cat is cute.\nThe dog is friendly.\nPython is awesome.\n", "awesome",
     ["Python is awesome.\n"]),
])
def test_filter_file(tmp_path, input_content, keyword, expected):
    input_file_path = tmp_path.joinpath("test_input.txt")
    with open(input_file_path, 'w') as file:
        file.write(input_content)

    output_file_path = tmp_path.joinpath("test_output.txt")
    filter_file(str(input_file_path), str(output_file_path), keyword)

    with open(output_file_path, 'r') as file:
        assert file.readlines() == expected
