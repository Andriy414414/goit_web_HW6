SELECT t.fullname, s2.name, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN subjects s2 ON s2.id = g.subject_id
JOIN teachers t ON t.id = s2.teacher_id
WHERE t.id = 1
GROUP BY s2.name 
