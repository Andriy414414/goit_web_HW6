SELECT s3.name, t.fullname
FROM subjects s3 
JOIN teachers t ON t.id = s3.teacher_id 
WHERE t.id = 3 
