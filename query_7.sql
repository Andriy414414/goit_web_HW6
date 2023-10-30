SELECT s2.name, g2.name, g.grade, s.fullname 
FROM grades g
JOIN subjects s2 ON s2.id = g.subject_id
JOIN students s on s.id = g.student_id 
JOIN [groups] g2 ON g2.id = s.group_id  
WHERE g2.id = 2 AND s2.id = 5

