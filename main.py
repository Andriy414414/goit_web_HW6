import sqlite3


def execute_query_1(sql1: str) -> list:
    with sqlite3.connect('univer.db') as con:
        cur = con.cursor()
        cur.execute(sql1)
        return cur.fetchall()


sql1 = """
SELECT s.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
LEFT JOIN students s on s.id = g.student_id 
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 5;
"""

print(f'\n 5 студентів із найбільшим середнім балом з усіх предметів: \n {execute_query_1(sql1)}')


def execute_query_2(sql2: str) -> list:
    with sqlite3.connect('univer.db') as con:
        cur = con.cursor()
        cur.execute(sql2)
        return cur.fetchall()


sql2 = """
SELECT s2.name, s.fullname, s.id, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN students s on s.id = g.student_id 
JOIN subjects s2 ON s2.id = g.subject_id 
WHERE s2.id = 6 
GROUP BY s.fullname 
ORDER BY average_grade DESC 
LIMIT 1;
"""

print(f'\n Cтудент із найвищим середнім балом з певного предмета: \n {execute_query_2(sql2)}')


def execute_query_3(sql3: str) -> list:
    with sqlite3.connect('univer.db') as con:
        cur = con.cursor()
        cur.execute(sql3)
        return cur.fetchall()


sql3 = """
SELECT s2.name, g2.name , ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN subjects s2 ON s2.id = g.subject_id
JOIN students s on s.id = g.student_id 
JOIN [groups] g2 ON g2.id = s.group_id  
WHERE s2.id = 8 
GROUP BY g2.name, s2.name 
ORDER BY average_grade DESC 
"""

print(f'\n Cередній бал у групах з певного предмета: \n {execute_query_3(sql3)}')


def execute_query_4(sql4: str) -> list:
    with sqlite3.connect('univer.db') as con:
        cur = con.cursor()
        cur.execute(sql4)
        return cur.fetchall()


sql4 = """
SELECT ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
"""
print(f'\n Cередній бал на потоці (по всій таблиці оцінок): \n {execute_query_4(sql4)}')


def execute_query_5(sql5: str) -> list:
    with sqlite3.connect('univer.db') as con:
        cur = con.cursor()
        cur.execute(sql5)
        return cur.fetchall()


sql5 = """
SELECT s3.name, t.fullname
FROM subjects s3 
JOIN teachers t ON t.id = s3.teacher_id 
WHERE t.id = 3 
"""
print(f'\n Курси, які читає певний викладач: \n {execute_query_5(sql5)}')


def execute_query_6(sql6: str) -> list:
    with sqlite3.connect('univer.db') as con:
        cur = con.cursor()
        cur.execute(sql6)
        return cur.fetchall()


sql6 = """
SELECT s3.fullname, g.name
FROM students s3 
JOIN groups g ON g.id = s3.group_id 
WHERE g.id = 3 
"""
print(f'\n Список студентів у певній групі: \n {execute_query_6(sql6)}')


def execute_query_7(sql7: str) -> list:
    with sqlite3.connect('univer.db') as con:
        cur = con.cursor()
        cur.execute(sql7)
        return cur.fetchall()


sql7 = """
SELECT s2.name, g2.name, g.grade, s.fullname 
FROM grades g
JOIN subjects s2 ON s2.id = g.subject_id
JOIN students s on s.id = g.student_id 
JOIN [groups] g2 ON g2.id = s.group_id  
WHERE g2.id = 2 AND s2.id = 5
"""
print(f'\n Оцінки студентів у окремій групі з певного предмета: \n {execute_query_7(sql7)}')


def execute_query_8(sql8: str) -> list:
    with sqlite3.connect('univer.db') as con:
        cur = con.cursor()
        cur.execute(sql8)
        return cur.fetchall()


sql8 = """
SELECT t.fullname, s2.name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN subjects s2 ON s2.id = g.subject_id
JOIN teachers t ON t.id = s2.teacher_id
WHERE t.id = 1
GROUP BY s2.name 
"""
print(f'\n Середній бал, який ставить певний викладач зі своїх предметів: \n {execute_query_8(sql8)}')


def execute_query_9(sql9: str) -> list:
    with sqlite3.connect('univer.db') as con:
        cur = con.cursor()
        cur.execute(sql9)
        return cur.fetchall()


sql9 = """
SELECT s.fullname, s2.name
FROM grades g
JOIN subjects s2 ON s2.id = g.subject_id
JOIN students s on s.id = g.student_id 
JOIN [groups] g2 ON g2.id = s.group_id  
WHERE s.id = 46 
GROUP BY s2.name 
"""
print(f'\n Список курсів, які відвідує студент: \n {execute_query_9(sql9)}')


def execute_query_10(sql10: str) -> list:
    with sqlite3.connect('univer.db') as con:
        cur = con.cursor()
        cur.execute(sql10)
        return cur.fetchall()


sql10 = """
SELECT s.fullname, s2.name, t.fullname
FROM grades g
JOIN subjects s2 ON s2.id = g.subject_id
JOIN students s on s.id = g.student_id 
JOIN teachers t  ON t.id = s2.teacher_id 
WHERE s.id = 41 and t.id = 1 
GROUP BY s2.id  
"""
print(f'\n Список курсів, які певному студенту читає певний викладач: \n {execute_query_10(sql10)}')

