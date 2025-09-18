import argparse
import os


def find_text_in_files(folder_path, search_text, find_all=True):
    results = []

    log_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    for file_path in log_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                if search_text in line:

                    words = line.split()
                    word_index = -1

                    for i, word in enumerate(words):
                        if search_text in word:
                            word_index = i
                            break

                    if word_index != -1:

                        start_index = max(0, word_index - 5)
                        end_index = min(len(words), word_index + 6)
                        context_words = words[start_index:end_index]
                        context = ' '.join(context_words)

                        results.append({
                            'file': os.path.basename(file_path),
                            'line': line_num,
                            'context': context
                        })

                        if not find_all:
                            break

    return results


def display_results(results, search_text):
    if not results:
        print(f"Текст '{search_text}' не найден в файлах логов")
        return

    print(f"\nНайдено {len(results)} совпадений:")

    for i, result in enumerate(results, 1):
        print(f"{i}. Файл: {result['file']}")
        print(f"Строка: {result['line']}")
        print(f"Контекст: {result['context']}")


def get_cmd_date():
    parser = argparse.ArgumentParser(description='Анализатор логов')
    parser.add_argument('folder_path', help='Путь к папке с логами')
    parser.add_argument('--text', required=True, help='Текст для поиска')
    parser.add_argument('--all', action='store_true',
                        help='Искать все вхождения (по умолчанию только первое)')

    args = parser.parse_args()
    print(args.folder_path)

    results = find_text_in_files(args.folder_path, args.text, args.all)
    display_results(results, args.text)


get_cmd_date()
