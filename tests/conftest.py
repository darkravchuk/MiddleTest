import pytest


# Фікстура для створення тимчасового файлу з тестовим вмістом
@pytest.fixture
def input_file(tmp_path):
    file_path = tmp_path.joinpath("test_input.txt")
    with open(file_path, 'w') as file:
        file.write("This is a test.\n"
                   "The cat is cute.\n"
                   "The dog is friendly.\n"
                   "Python is awesome.\n")
    return str(file_path)
