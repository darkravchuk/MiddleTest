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


def write_file(output_file: str, lines: list) -> None:
    """
    Функція для запису списку рядків у файл.

    :param output_file: Ім'я файлу для запису результатів
    :type output_file: str
    :param lines: Список рядків для запису
    :type lines: list
    """
    with open(output_file, 'w') as file:
        for line in lines:
            file.write(line)


def filter_file(input_file: str, output_file: str, keyword: str) -> None:
    """
    Головна функція для фільтрації файлу за певним ключовим словом.

    :param input_file: Шлях до вхідного файлу
    :type input_file: str
    :param output_file: Шлях до вихідного файлу
    :type output_file: str
    :param keyword: Ключове слово для фільтрації
    :type keyword: str
    """
    lines = read_file(input_file)
    filtered_lines = filter_lines(lines, keyword)
    write_file(output_file, filtered_lines)


if __name__ == "__main__":
    try:
        input_file = "test.txt"  # Ваш вхідний файл
        output_file = "filtered.txt"  # Вихідний файл, куди буде записаний результат
        keyword = "cat"  # Ключове слово, яке потрібно знайти

        filter_file(input_file, output_file, keyword)
    except:
        print('An error occurred')