SELECT s.fullname, s2.name
FROM grades g
JOIN subjects s2 ON s2.id = g.subject_id
JOIN students s on s.id = g.student_id 
JOIN [groups] g2 ON g2.id = s.group_id  
WHERE s.id = 46 
GROUP BY s2.name 
