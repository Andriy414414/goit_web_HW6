SELECT s2.name, g2.name , ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN subjects s2 ON s2.id = g.subject_id
JOIN students s on s.id = g.student_id 
JOIN [groups] g2 ON g2.id = s.group_id  
WHERE s2.id = 8 
GROUP BY g2.name, s2.name 
ORDER BY average_grade DESC 
