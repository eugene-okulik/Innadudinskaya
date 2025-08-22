import mysql.connector as mysql
import random


def student_creation(cursor):
    cursor.execute("INSERT into students (name, second_name, group_id) values ('Sergey', 'Mikulskiy', NULL)")

    student_id_db = cursor.lastrowid
    cursor.execute(f'SElECT * from students where id = {student_id_db}')
    print(cursor.fetchone())
    return student_id_db


def books_creation(student_id, cursor):
    insert_books = 'INSERT into books (title, taken_by_student_id) values (%s, %s)'
    cursor.executemany(
        insert_books, [
            ('Python for AQA', student_id),
            ('Python for beginners', student_id)
        ]
    )


def group_creation(cursor):
    cursor.execute(
        "INSERT into `groups` (title, start_date, end_date) values ('Python AQA new testers', 'nov 2024', 'nov 2025')")
    group_id = cursor.lastrowid
    cursor.execute(f'SElECT * from `groups` where id = {group_id}')
    print(cursor.fetchone())
    return group_id


def update_student(student_id, group_id, cursor):
    cursor.execute('UPDATE students SET group_id= %s where id = %s', (group_id, student_id))


def subjects_creation(cursor, subject_name):
    cursor.execute("INSERT into subjects (title) values (%s)", (subject_name,))
    subject_id_db = cursor.lastrowid
    cursor.execute(f'SElECT * from subjects where id = {subject_id_db}')
    print(cursor.fetchone())
    return subject_id_db


def lessons_creation(cursor, lesson_name, subject_id):
    cursor.execute("INSERT into lessons(title, subject_id) values(%s, %s)", (lesson_name, subject_id))
    lesson_id_db = cursor.lastrowid
    cursor.execute(f'SElECT * from lessons where id = {lesson_id_db}')
    print(cursor.fetchone())
    return lesson_id_db


def marks_creation(lesson_id, cursor):
    insert_marks = "INSERT into marks(value, lesson_id, student_id) values(%s, %s, %s)"
    # Создаем по 1 случайной оценке от 7 до 10 для каждого занятия
    marks = [str(random.randint(7, 10)) for _ in range(1)]
    data = [(mark, lesson_id, student_id) for mark in marks]
    cursor.executemany(insert_marks, data)


def student_grades(student_id, cursor):
    cursor.execute('SELECT value FROM marks where student_id=%s', (student_id,))
    grades = cursor.fetchall()
    print(f'оценки студента: {grades}')


def student_books(student_id, cursor):
    cursor.execute('SELECT title FROM books where taken_by_student_id=%s', (student_id,))
    books = cursor.fetchall()
    print(f'книги студента: {books}')


def all_informatuin_about_student(student_id, cursor):
    select_final_query = '''
    SELECT * FROM students
    join `groups` on students.group_id=`groups`.id
    join books on students.id=books.taken_by_student_id
    join marks on students.id=marks.student_id
    join lessons on marks.lesson_id=lessons.id
    join subjects on lessons.subject_id=subjects.id where students.id=%s
    '''
    cursor.execute(select_final_query, (student_id,))
    results = cursor.fetchall()
    print(f'вся информация о студенте: {results}')


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

student_id = student_creation(cursor)

books_creation(student_id, cursor)

group_id = group_creation(cursor)

update_student(student_id, group_id, cursor)

subject_id1 = subjects_creation(cursor, 'API testing', )
subject_id2 = subjects_creation(cursor, 'UI testing', )

lesson_id1 = lessons_creation(cursor, 'lesson1', subject_id1)
lesson_id2 = lessons_creation(cursor, 'lesson2', subject_id1)
lesson_id3 = lessons_creation(cursor, 'lesson3', subject_id2)
lesson_id4 = lessons_creation(cursor, 'lesson4', subject_id2)

marks_creation(lesson_id1, cursor)
marks_creation(lesson_id2, cursor)
marks_creation(lesson_id3, cursor)
marks_creation(lesson_id4, cursor)

student_grades(student_id, cursor)

student_books(student_id, cursor)

all_informatuin_about_student(student_id, cursor)

db.commit()
db.close()
