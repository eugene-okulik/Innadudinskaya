import csv
import os
import mysql.connector as mysql
import dotenv


def read_file():
    with open(eugene_okulik_file_path, newline='') as csv_file:
        file_data = csv.DictReader(csv_file)
        file_result = []
        for row in file_data:
            print(row)
            file_result.append(row)
        return file_result


def student_count(student_name, student_second_name, group_title, book_title, subject_title,
                  lesson_title, mark_value, cursor_def):
    select_final_query = '''
    SELECT count(*) FROM students
    join `groups` on students.group_id=`groups`.id
    join books on students.id=books.taken_by_student_id
    join marks on students.id=marks.student_id
    join lessons on marks.lesson_id=lessons.id
    join subjects on lessons.subject_id=subjects.id 
    where
    students.name=%s 
    and students.second_name=%s
    and `groups`.title =%s
    and books.title=%s
    and subjects.title=%s
    and lessons.title=%s
    and marks.value=%s
    '''
    cursor_def.execute(select_final_query, (student_name, student_second_name, group_title, book_title, subject_title,
                                            lesson_title, mark_value))
    results = cursor_def.fetchall()

    if results[0]["count(*)"] == 0:
        student_data = {
            'name': student_name,
            'second_name': student_second_name,
            'group_title': group_title,
            'book_title': book_title,
            'subject_title': subject_title,
            'lesson_title': lesson_title,
            'mark_value': mark_value
        }
        print(f'вся информация о студенте: {student_data}')
    else:
        print(f'этот пользователь есть в базе: {student_name}, {student_second_name}')


dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_okulik_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

cursor = db.cursor(dictionary=True)

students = read_file()

for student in students:
    student_count(student['name'], student['second_name'], student['group_title'],
                  student['book_title'], student['subject_title'], student['lesson_title'],
                  student['mark_value'], cursor)

db.close()
