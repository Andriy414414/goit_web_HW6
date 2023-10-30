SELECT s.fullname, s2.name, t.fullname
FROM grades g
JOIN subjects s2 ON s2.id = g.subject_id
JOIN students s on s.id = g.student_id 
JOIN teachers t  ON t.id = s2.teacher_id 
WHERE s.id = 41 and t.id = 1 
GROUP BY s2.id  
