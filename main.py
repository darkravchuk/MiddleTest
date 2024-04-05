def read_file(file_path: str) -> list:
    """
    Функція для зчитування вмісту файлу та повернення списку рядків.

    :param file_path: Шлях до файлу
    :type file_path: str
    :return: Список рядків з файлу
    :rtype: list
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines