def read_file(input_file: str) -> list[str]:
    """
    Read the content of a file.

    Args:
        input_file (str): The path to the input file.

    Returns:
        list[str]: A list containing each line of the file as a string.
    """
    with open(input_file, 'r') as f:
        lines = f.readlines()
        return lines
