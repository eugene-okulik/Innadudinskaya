INSERT into students (name, second_name, group_id) values ('Inna', 'Dudinskaya', NULL)
SELECT * FROM students WHERE second_name='Dudinskaya' -- находим здесь id созданного student
INSERT into books (title, taken_by_student_id) values ('Python for AQA', 20842)
INSERT into books (title, taken_by_student_id) values ('Python for beginners', 20842)
INSERT into `groups` (title, start_date, end_date) values ('Python AQA testers', 'nov 2024', 'nov 2025')
SELECT * FROM `groups` where title='Python AQA testers' -- находим здесь id созданной группы
UPDATE students SET group_id=5456 where id=20842 -- созданного студента присоединяем к нашей группе
INSERT into subjets (title) values ('Python basics1')
INSERT into subjets (title) values ('API testing')
INSERT into subjets (title) values ('UI testing')
SELECT * FROM subjets where title='Python basics1' -- находим здесь id созданного subject
SELECT * FROM subjets where title='API testing' -- находим здесь id созданного subject
SELECT * FROM subjets where title='UI testing' -- находим здесь id созданного subject

INSERT into lessons (title, subject_id) values ('Conditions and Loops', 11575)
INSERT into lessons (title, subject_id) values ('Loops and functions', 11575)

INSERT into lessons (title, subject_id) values ('API testing1', 11576)
INSERT into lessons (title, subject_id) values ('API testing2', 11576)

INSERT into lessons (title, subject_id) values ('UI testing1', 11577)
INSERT into lessons (title, subject_id) values ('UI testing2', 11577)

SELECT * FROM lessons where title='Conditions and Loops' -- здесь находим id созданных lessons
SELECT * FROM lessons where title='Loops and functions'
SELECT * FROM lessons where title='API testing1'
SELECT * FROM lessons where title='API testing2'
SELECT * FROM lessons where title='UI testing1'
SELECT * FROM lessons where title='UI testing2'

INSERT into marks (value, lesson_id, student_id) values (10, 11600, 20842)
INSERT into marks (value, lesson_id, student_id) values (10, 11601, 20842)
INSERT into marks (value, lesson_id, student_id) values (9, 11602, 20842)
INSERT into marks (value, lesson_id, student_id) values (9, 11603, 20842)
INSERT into marks (value, lesson_id, student_id) values (8, 11604, 20842)
INSERT into marks (value, lesson_id, student_id) values (8, 11605, 20842)

SELECT value FROM marks where student_id=20842 -- получили все оценки нашего студента

SELECT title FROM  books where taken_by_student_id=20842 -- получили все книги, которые у студента

SELECT * FROM students
join `groups` on students.group_id=`groups`.id
join books on students.id=books.taken_by_student_id
join marks on students.id=marks.student_id
join lessons on marks.lesson_id=lessons.id
join subjets on lessons.subject_id=subjets.id where students.id=20842 -- вывели всю информацию о студенте


