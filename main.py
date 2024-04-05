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


def filter_lines(lines: list, keyword: str) -> list:
    """
    Функція для фільтрації рядків за певним ключовим словом.

    :param lines: Список рядків для фільтрації
    :type lines: list
    :param keyword: Ключове слово для фільтрації
    :type keyword: str
    :return: Список відфільтрованих рядків
    :rtype: list
    """
    filtered_lines = [line for line in lines if keyword in line]
    return filtered_lines