-- select score and name where the name is not null or empty ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL and name !=''
ORDER BY score DESC;
