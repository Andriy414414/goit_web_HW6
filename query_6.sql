SELECT s3.fullname, g.name
FROM students s3 
JOIN groups g ON g.id = s3.group_id 
WHERE g.id = 3 
