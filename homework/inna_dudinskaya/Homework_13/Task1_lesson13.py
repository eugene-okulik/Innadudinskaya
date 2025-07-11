import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_okulik_file_path)

with open(eugene_okulik_file_path, encoding='utf-8') as eugene_okulik_file:
    for line in eugene_okulik_file:
        parts = line.split(' - ')
        if len(parts) < 2:
            continue

        number_part = parts[0].split('. ')[0]
        date_str = parts[0].split('. ')[1]
        action = parts[1].strip()

        date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')

        if number_part == '1':
            new_date = date + datetime.timedelta(days=7)
            print(f'1. Новая дата: {new_date}')
        elif number_part == '2':
            weekday = date.strftime('%A')
            print(f"2. Это был {weekday}")

        elif number_part == '3':
            now = datetime.datetime.now()
            days_ago = (now - date).days
            print(f'3. Это было {days_ago} дней назад')
